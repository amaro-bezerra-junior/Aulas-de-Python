largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
caractere = "#"

y = 1

while y <= altura:
	print(caractere * largura, end = "")
	print()
	y += 1
	while y > 1 and y < altura:
		print(caractere + " " * (largura - 2) + caractere)
		y += 1