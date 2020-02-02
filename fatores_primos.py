numero = int(input("Digite um número maior que zero: "))

fator = 2
multiplicidade = 0

while numero > 1:
	while numero % fator == 0:
		multiplicidade += 1
		numero = numero / fator
	if multiplicidade > 0:
		print("Fator",fator,"Multiplicidade",multiplicidade)
	fator += 1
	multiplicidade = 0