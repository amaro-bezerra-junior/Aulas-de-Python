print("***************Consumo de Energia***************")

print("Selecione uma das categorias abaixo para verificar o consumo de energia:")

print("Digite R para consumo residencial.")#informa apenas a categoria a ser informada.
print("Digite I para consumo industrial.")
print("Digite C para consumo comercial.")

categoria = input("Informe o tipo de instalação a ser verificada: ")#entrada de categoria
consumo = float(input("Informe a quantidade de Kw/h consumidos: "))#entrada de consumo.

if categoria == "R" or categoria == "r":
	if consumo <= 500:
		preco = 0.40
	else:
		preco = 0.65
elif categoria == "C" or categoria == "c":
	if consumo <= 1000:
		preco = 0.55
	else:
		preco = 0.60
elif categoria == "I" or categoria == "i":
	if consumo <= 5000:
		preco = 0.55
	else:
		preco = 0.60
else:
	preco = 0
	print("Categoria não localizada. Gentileza escolher entre as categorias C, I ou R.")
valor = (preco * consumo)
print(f"O valor da fatura à pagar é de R$%7.2f"%valor)