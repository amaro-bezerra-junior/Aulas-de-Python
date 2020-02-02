print("Receba três números e imprima o maior e o menor.")

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

menor = a #verificando o menor valor das variáveis
maior = a #verificando o maior valor das variáveis

if b < a and b < c:
	menor = b
if c < a and c < b:
	menor = c
if b > a and b > c:
	maior = b
if c > a and c > b:
	maior = c
print("O maior valor digitado foi",maior,"e o menor valor digitado foi",menor)