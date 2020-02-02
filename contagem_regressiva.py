print("Contagem regressiva de um foguete!")

contagem = int(input("Informe o início da contagem regressiva: "))#entrada de dados.

x = contagem#variável "x" recebe a entrada de dados da variável "contagem".

from time import sleep#importando pacote de dados time spleep.

while x >= 0:#enquanto o valor da variável "x" for maior que 0, continue a contagem.
	print(x)#saida dos valores de "x"
	sleep(1)#função spleep com contagem de 1segundo.
	x = x - 1#subtrai o valor de "x" - 1.
print("Fogo...")#quando o valor de "x" for igual a 0, imprimi "Fogo..."