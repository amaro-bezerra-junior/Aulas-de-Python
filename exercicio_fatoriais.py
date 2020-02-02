print("********** Descubra o fatorial dos números inteiros positivos. **********")

n = int(input("Digite um número inteiro: "))

while n >= 0:
	fatorial = 1
	while n > 1:
		fatorial = fatorial * n
		n = n - 1
	print(fatorial)
	n = int(input("Digite um número inteiro: "))
	if n < 0:
		print("O programa foi encerrado porque você digitou um número negativo!")