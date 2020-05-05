# -*- coding: utf-8 -*-
"""Desafio_Final_Amaro-Junior_Bemol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KtPwi6qedD0fdFG0EK_XquMJanAupIb3
"""

import pandas as pd

print('Realizando Leitura dos Arquivos...')

df_detalhamento1 = pd.read_excel('detalhamento.xlsx', sheet_name = 'AM', skiprows= 1)

df_detalhamento2 = pd.read_excel('detalhamento.xlsx', sheet_name = 'RR', skiprows= 1)

df_detalhamento3 = pd.read_excel('detalhamento.xlsx', sheet_name = 'RO', skiprows= 1)

df_detalhamento4 = pd.read_excel('detalhamento.xlsx', sheet_name = 'AC', skiprows= 1)

df_vendas = pd.read_csv('vendas.csv', sep = '|', skiprows = 0, encoding = 'utf-8')

df_detalhamento1

df_detalhamento2

df_detalhamento3

df_detalhamento4

df_vendas

print('Iniciando Tratamento das Informações...')

df_detalhamento1 = df_detalhamento1.rename(columns = {'NomeFantasia':'Loja','Escritório de vendas':'Escritório_de_Vendas', 'UF':'UF', 'Operadora':'Operadora', 'Vlookup Bruto':'Valor_Bruto'})

df_detalhamento2 = df_detalhamento2.rename(columns = {'NomeFantasia':'Loja','Escritório de vendas':'Escritório_de_Vendas', 'UF':'UF', 'Operadora':'Operadora', 'Vlookup Bruto':'Valor_Bruto'})

df_detalhamento3 = df_detalhamento3.rename(columns = {'NomeFantasia':'Loja','Escritório de vendas':'Escritório_de_Vendas', 'UF':'UF', 'Operadora':'Operadora', 'Vlookup Bruto':'Valor_Bruto'})

df_detalhamento4 = df_detalhamento4.rename(columns = {'NomeFantasia':'Loja','Escritório de vendas':'Escritório_de_Vendas', 'UF':'UF', 'Operadora':'Operadora', 'Valor Bruto':'Valor_Bruto'})

df_vendas = df_vendas.rename(columns = {'Escritório de vendas':'Escritório_de_Vendas', 'Fornecedor':'Operadora', 'Material':'Material', 'Data':'Data', 'Valor Liquido':'Valor_Liquido'})

df_detalhamento1

df_detalhamento2

df_detalhamento3

df_detalhamento4

df_vendas

df_detalhamento1 = df_detalhamento1.drop(['UF'], axis = 'columns')

df_detalhamento2 = df_detalhamento2.drop(['UF'], axis = 'columns')

df_detalhamento3 = df_detalhamento3.drop(['UF'], axis = 'columns')

df_detalhamento4 = df_detalhamento4.drop(['UF'], axis = 'columns')

df_vendas = df_vendas.drop(['Material', 'Data'], axis = 'columns')

df_detalhamento1

df_detalhamento2

df_detalhamento3

df_detalhamento4

df_vendas

df_detalhamento1.dtypes

df_detalhamento2.dtypes

df_detalhamento3.dtypes

df_detalhamento4.dtypes

df_vendas.dtypes

df_vendas['Valor_Liquido'] = df_vendas['Valor_Liquido'].astype(int)

df_vendas.dtypes

df_vendas

df_detalhamento = pd.concat([df_detalhamento1,df_detalhamento2,df_detalhamento3,df_detalhamento4])

df_detalhamento

df_detalhamento = df_detalhamento.reset_index(drop = True)

df_detalhamento

df_vendas = df_vendas.reset_index(drop = True)

df_vendas

df_vendas = df_vendas.groupby(['Escritório_de_Vendas', 'Operadora']).agg({'Valor_Liquido':'sum'}).reset_index(drop = False)

df_vendas

df_relatorio_final = pd.merge(df_detalhamento, df_vendas,  on = ['Escritório_de_Vendas','Operadora'], how = 'left')

df_relatorio_final

df_relatorio_final.fillna(0)

df_relatorio_final = df_relatorio_final.drop(['Escritório_de_Vendas'], axis = 'columns')

df_relatorio_final

def verificar_status(Valor_Liquido, Valor_Bruto):
  if (Valor_Liquido == Valor_Bruto):
    return 'Ok'
  else:
    return 'Apresenta Divergência'

df_relatorio_final['Status'] = df_relatorio_final.apply(lambda row: verificar_status(row['Valor_Liquido'], row['Valor_Bruto']), axis = 'columns')

df_relatorio_final

print('Gerando Relatório...')

df_relatorio_final.columns = ['Loja', 'Operadora', 'Valor_Liquido', 'Valor_Bruto', 'Status']

df_relatorio_final

df_relatorio_final.to_csv('Relatório_Final.csv', sep = ';')

writer = pd.ExcelWriter('Relatório_Final.xlsx')

df_relatorio_final.to_excel(writer, sheet_name = 'Conciliação', index = False)

writer.save()

print('Relatório Gerado com Sucesso!')

input()