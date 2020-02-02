print("Indica a existência de números iguais.")

n = int(input("Digite um número: "))

num1 = n % 10
num2 = n // 10

adjacente_iguais = False
y = 0

while num2 > 0 and not adjacente_iguais:
        num3 = num2 % 10
        if num3 == num1:
                adjacente_iguais = True
        else:
                y = y + 1
        num1 = num3
        num2 = num2 // 10
if adjacente_iguais:
	print("O número",n,"possui dois digitos adjacentes iguais!")
else:
	print("O número",n,"não possui digitos adjacentes iguais!")
