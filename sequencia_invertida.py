sequencia = []
while True:
	numero = int(input("Digite um número: "))
	if numero == 0: break
	sequencia.append(numero)
for i in reversed(sequencia):
	print(i)
