print("Programa calcula a soma do número informado.")

n = int(input("Informe o valor de n: "))

i = 0

while n > 0:
	restante = (n % 10)
	n = (n - restante) // 10
	i = i + restante
print(i)
