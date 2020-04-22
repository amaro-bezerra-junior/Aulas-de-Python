
# coding: utf-8

# # <center> Support Vector Machine </center>
# ## Professor: Victor Venites
# ## Aluno: Amaro Junior
# ## Data: 14/04/2020
# ## Aula: 07

# ## 1. Importando as Bibliotecas de Python
# - E Verificando o Ambiente

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# - Print Working Directory

# In[ ]:


pwd


# - Minha Versão do Python
# - Python 3.7.3

# In[ ]:


get_ipython().system('python  --version')


# ## 2. Base de Dados OR
# - Verdadeiro OU Falso

# In[ ]:


df_OR = pd.read_excel("OR.xlsx", index_col = "Lição")
df_OR


# In[ ]:


cores = ["blue", "orange", "orange", "orange"]
plt.scatter(df_OR["Entrada_Um"], df_OR["Entrada_Dois"], c = cores)
plt.title("Porta Lógica OR")
plt.xlabel("Entrada_Um")
plt.ylabel("Entrada_Dois")
plt.savefig("Gráfico_OR.jpg")
plt.show()


# ## 3. Base de Dados AND
# - Verdadeiro E Falso

# In[ ]:


df_AND = pd.read_excel("AND.xlsx", index_col = "Lição")
df_AND


# In[ ]:


cores = ["blue", "blue", "blue", "orange"]
plt.scatter(df_AND["Entrada_Um"], df_AND["Entrada_Dois"], c = cores)
plt.title("Porta Lógica AND")
plt.xlabel("Entrada_Um")
plt.ylabel("Entrada_Dois")
plt.savefig("Gráfico_AND.jpg")
plt.show()


# ## 4. Vamos Criar Nosso "BigData" de XOR

# In[ ]:


Entrada_Um = [0, 0, 1, 1]
Entrada_Dois = [0, 1, 0, 1]
Saida_XOR = [0, 1, 1, 0]
Colunas = ["Entrada_Um", "Entrada_Dois", "Saida_XOR"]
Indice = [1, 2, 3, 4]


# In[ ]:


df_XOR = pd.DataFrame([], columns = Colunas, index = Indice)
df_XOR


# In[ ]:


df_XOR["Entrada_Um"] = Entrada_Um
df_XOR["Entrada_Dois"] = Entrada_Dois
df_XOR["Saida_XOR"] = Saida_XOR
df_XOR


# In[ ]:


cores = ["blue", "orange", "orange", "blue"]
plt.scatter(df_XOR["Entrada_Um"], df_XOR["Entrada_Dois"], c = cores)
plt.title("Porta Lógica XOR")
plt.xlabel("Entrada_Um")
plt.ylabel("Entrada_Dois")
plt.savefig("Gráfico_XOR.jpg")
plt.show()


# ## 5. Modelo Support Vector Machine
# - Machina de Vetor de Suporte

# In[ ]:


df_OR


# ### 5.2. Versão do SkLearn

# In[ ]:


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix


# #### 5.2.1. Classificando OR

# In[ ]:


X_OR = df_OR.iloc[:, 0:-1]
y_OR = df_OR.iloc[:, -1]
y_OR


# In[ ]:


svm_clf_OR = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C = 0.5, loss = "hinge", penalty='l2')),
])
svm_clf_OR.fit(X_OR, y_OR)


# #### 5.2.1.1. Resultados OR

# In[ ]:


svm_clf_OR.predict([[0, 0]])


# In[ ]:


svm_clf_OR.predict([[0, 1]])


# In[ ]:


svm_clf_OR.predict([[1, 0]])


# In[ ]:


svm_clf_OR.predict([[1, 1]])


# #### 5.2.1.2. Matriz de Confusão
# - A função considera os rótulos na ordem de chegada
# - 0 Como sendo a primeira classificação
# - 1 Como sendo a segunda classificação

# In[ ]:


Predicao_OR = svm_clf_OR.predict(X_OR)
confusion_matrix(y_OR, Predicao_OR)


# In[ ]:


df_OR_Predicao = df_OR.copy()
df_OR_Predicao["Predicao"] = Predicao_OR
df_OR_Predicao


# #### 5.2.1.1. Plotando o Vetor de Suporte
# - mlxtend
# - Pacote para imprimir Gráficos de Classificação bonitos, tipo nos livros
# - Herda do MatPlotLib
# - pip => Python Installer Package

# In[ ]:


get_ipython().system('pip install mlxtend')


# In[ ]:


from mlxtend.plotting import plot_decision_regions


# In[ ]:


Parametros_Plot_mlxtend = {"X" : X_OR.values ,
                           "y" : y_OR.values ,
                           "clf" : svm_clf_OR ,
                           "legend" : 2
                          }
plot_decision_regions(**Parametros_Plot_mlxtend)
plt.xlabel(X_OR.columns[0], size=14)
plt.ylabel(X_OR.columns[1], size=14)
plt.title('Fronteira Separadora do SVM para OR', size=16)


# ### 5.2.2. Classificando AND

# In[ ]:


X_AND = df_AND.iloc[:, 0:-1]
y_AND = df_AND.iloc[:, -1]
svm_clf_AND = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C = 1, loss = "hinge", penalty='l2')),
])
svm_clf_AND.fit(X_AND, y_AND)
Predicao_AND = svm_clf_AND.predict(X_AND)
confusion_matrix(y_AND, Predicao_AND)


# #### 5.2.2.1. Plotando o Vetor de Suporte

# In[ ]:


Parametros_Plot_mlxtend = {"X" : X_AND.values ,
                           "y" : y_AND.values ,
                           "clf" : svm_clf_AND ,
                           "legend" : 2
                          }
plot_decision_regions(**Parametros_Plot_mlxtend)
plt.xlabel(X_AND.columns[0], size=14)
plt.ylabel(X_AND.columns[1], size=14)
plt.title('Fronteira Separadora do SVM para AND', size=16)


# ### 5.2.3. Classificando XOR

# In[ ]:


X_XOR = df_XOR.iloc[:, 0:-1]
y_XOR = df_XOR.iloc[:, -1]
svm_clf_XOR = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C = 1, loss = "squared_hinge", penalty='l2')),
])
svm_clf_XOR.fit(X_XOR, y_XOR)
Predito_XOR = svm_clf_XOR.predict(X_XOR)
Predito_XOR


# - Por que não deu certo acima?

# In[ ]:


from sklearn.preprocessing import PolynomialFeatures


# In[ ]:


X_XOR = df_XOR.iloc[:, 0:-1]
y_XOR = df_XOR.iloc[:, -1]
svm_clf_XOR = Pipeline([
    ("poly_features", PolynomialFeatures(degree = 2)),
    ("linear_svc", LinearSVC(C = 1, loss = "squared_hinge", penalty='l2', )),
])
svm_clf_XOR.fit(X_XOR, y_XOR)
Predito_XOR = svm_clf_XOR.predict(X_XOR)
confusion_matrix(y_XOR, Predito_XOR)


# In[ ]:


df_XOR_Resultado = df_XOR.copy()
df_XOR_Resultado["Predito_XOR"] = Predito_XOR
df_XOR_Resultado


# #### 5.2.3.1. Plotando o Vetor de Suporte

# In[ ]:


Parametros_Plot_mlxtend = {"X" : X_XOR.values ,
                           "y" : y_XOR.values ,
                           "clf" : svm_clf_XOR ,
                           "legend" : 2
                          }
plot_decision_regions(**Parametros_Plot_mlxtend)
plt.xlabel(X_XOR.columns[0], size=14)
plt.ylabel(X_XOR.columns[1], size=14)
plt.title('Fronteira Separadora do SVM para XOR', size=16)


# ### 5.2.4. Classificando Tipos de Cancer

# In[ ]:


df_Cancer = pd.read_excel("breastCancer.xlsx", index_col = "id")
df_Cancer.head()


# In[ ]:


X_Cancer = df_Cancer.iloc[:, 0:-1]
y_Cancer = df_Cancer.iloc[:, -1]
svm_clf_Cancer = Pipeline([
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C = 1, loss = "hinge", penalty='l2', max_iter = 1000)),
])
svm_clf_Cancer.fit(X_Cancer, y_Cancer)
Predicao_Cancer = svm_clf_Cancer.predict(X_Cancer)
confusion_matrix(y_Cancer, Predicao_Cancer)


# In[ ]:


df_Cancer_Resultado = df_Cancer.copy()
df_Cancer_Resultado["Predicao_Cancer"] = Predicao_Cancer
df_Cancer_Resultado.head()


# In[ ]:


from sklearn.metrics import accuracy_score


# In[ ]:


Acuracia_Cancer = accuracy_score(y_Cancer, Predicao_Cancer)
Acuracia_Cancer = round(Acuracia_Cancer * 100, 2)
Acuracia_Cancer


# In[ ]:


valor = 10
plt.figure(figsize = (16, 6))
Parametros_Plot_mlxtend = {"X" : X_Cancer.values,
                           "y" : y_Cancer.values,
                           "clf" : svm_clf_Cancer,
                           "filler_feature_values" : {2: valor, 3: valor, 4: valor, 5: valor, 6: valor, 7: valor, 8: valor},
                           "filler_feature_ranges" : {2: valor, 3: valor, 4: valor, 5: valor, 6: valor, 7: valor, 8: valor}
                          }
plot_decision_regions(**Parametros_Plot_mlxtend)
plt.xlabel(X_Cancer.columns[0], size = 14)
plt.ylabel(X_Cancer.columns[1], size = 14)
plt.title(f'Fronteira Separadora do SVM para Tipos de Cancer com {Acuracia_Cancer}%', size = 16)
plt.show()

