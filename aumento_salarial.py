print("Cálculo do aumento salarial.")

salario = float(input("Informe o seu salário: "))

base = salario
if base	>= 1250:
	base = (base + (base * 0.1))
	print("Reajuste de 10%. Sálario corrigido para R$",base)
if base <= 1000:
	base = (base + (base * 0.15))
	print("Reajuste de 15%. Sálario corrigido para R$",base)