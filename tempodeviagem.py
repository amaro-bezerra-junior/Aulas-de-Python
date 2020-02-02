print("**********Calule o tempo de viagem**********") #informa a finalidade do programa.

distância = float(input("Qual a distância a ser percorrida: ")) #entrada de dados referente a distância percorrida.
velocidade = int(input("Qual a velocidade média esperada: ")) #entrada de dados referente a velocidade media.

hora_decimal = (distância / velocidade) #variável recebe os valores das variáveis "distância" e "velocidade" realizando a divisão.
hora = int(hora_decimal) #variável "hora" recebe o resultado da variável "hora_decimal" de forma inteira.
dias = (hora // 24) #variável "dia" recebe o resultado da variável "hora"(resultado inteiro) e é divida de forma inteira por 24h.
horas_restantes = hora % 24 #variável "horas_restantes" receber o valor da variável "hora" e é dividido pela sobra de 24h.
minuto_decimal = (hora - hora_decimal) #variável "minuto_decimal" recebe a subtração das variáveis "hora" e "hora_decimal".
minuto = abs(int(minuto_decimal * 60)) #variável "minuto" recebe a multiplicação da variável "minuto_decimal" por 60minutos e retorna o resultado de forma absoluta.

print("O tempo de viagem é",dias,"dias",horas_restantes,"horas e",minuto,"minutos.") #saída de dados.
