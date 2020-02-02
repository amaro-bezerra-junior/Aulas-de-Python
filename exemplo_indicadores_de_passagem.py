print("Programa verificar se os números informados estão em ordem decrescente.")

decrescente = True

primeiro = int(input("Digite o primeiro número da sequência: "))

proximo = 1

while proximo != 0 and decrescente:
	proximo = int(input("Digite o próximo número da sequência: "))
	if proximo > primeiro:
		decrescente = False
		primeiro = proximo
if decrescente:
	print("A sequência está em ordem decrescente!")
else:
	print("A sequência não está em ordem decrescente!")