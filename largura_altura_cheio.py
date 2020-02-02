largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
caractere = "#"

def retangulo(caractere, largura, altura):
	linha_cheia = (caractere * largura)
	if largura > 2:
		linha_vazia = caractere + (caractere * (largura - 2)) + caractere
	else:
		linha_vazia = linha_cheia
	if altura >= 1:
		print(linha_cheia)
	for i in range(altura - 2):
		print(linha_vazia)
	if altura >= 2:
		print(linha_cheia)
retangulo(caractere, largura, altura)