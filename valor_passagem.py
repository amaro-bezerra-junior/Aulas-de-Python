print("Descubra o valor da passagem pelo KM rodado.")

km_a_rodar = float(input("Informe o KM a ser percorrido: "))

base = km_a_rodar

if base <= 200:
	base = base * 0.5
	print("O valor da passagem é de R$",base)
else:
	base = base * 0.45
	print("O valor da passagem é de R$",base)