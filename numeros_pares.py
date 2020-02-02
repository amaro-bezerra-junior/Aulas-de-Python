print("Números pares com a função While.")

fim = int(input("Informe o último número a imprimir na contagem de números pares: "))

x = 0

while x <= fim:
	if x % 2 == 0:
		print(x)
	x = x + 1