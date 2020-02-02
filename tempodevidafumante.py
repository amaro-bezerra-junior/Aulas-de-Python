print("**********Tempo de vida de um fumante**********")

quantidade_cigarros = int(input("Informe a quantidade de cigarros consumidos ao dia: "))#entrada de dados
tempo_fumante = int(input("É fumante há quanto tempo: "))#entrada de dados

segundos = ((quantidade_cigarros * 10) * (tempo_fumante * 365)) * 60#retorna o valor em segundos.

dias = segundos // 86400 #a variável "dias" recebe a divisão inteira referente a entrada da variável "segundos" por 86400 (equivalente a multiplicação de 60seg*60min*24h). 
segundos_restantes = segundos % 86400 #a variável "segundos_restantes" recebe a entrada da variável "segundos" onde é realizada o resto da divisão por 86400 (equivalente a multiplicação de 60seg*60min*24h).
horas = segundos_restantes // 3600 #a vaariável "horas" recebe o resultado da variável "segundos_restantes" e é dividida por inteiro por 3600 (equivalente a multiplicação de 60seg*60min). 
segundos_restantes = segundos_restantes % 3600 #a variável "segundos_restantes" recebe o valor da variável "segundos_restantes" e realizamos a sobra da divisão por 3600 (equivalente a multiplicação de 60seg*60min).
minutos = segundos_restantes // 60 #a variável "minutos" recebe o valor de "segundos_restantes" e é dividida por inteiro por 60min.
segundos_restantes = minutos % 60 #a variável "segundos_restantes" recebe o valor da variável "segundos_restantes" e é dividida pela sobra de 60min.

print("Você perderá",dias,"dias",horas,"horas",minutos,"minutos e",segundos_restantes,"segundos como fumante!")