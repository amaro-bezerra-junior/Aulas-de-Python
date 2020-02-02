n = int(input("Digite um número inteiro: "))

y = 0
i = 1

while i <= n:
	if n % i == 0:
		y += 1
	i += 1
if y == 2:
	print("primo")
else:
	print("não primo")