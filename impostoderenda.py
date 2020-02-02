print("**********Cálculo do Imposto de Renda**********")

salario = float(input("Informe o seu sálario para realização do cálculo de imposto: "))#entrada de dados.

base = salario#recebe o valor informado da variável "salario".
imposto = 0#a variável recebe o valor inicial 0.
if base > 3000:
	imposto = imposto + ((base - 3000) * 0.35)
	base = 3000
if base > 1000:
	imposto = imposto + ((base - 1000) * 0.20)
	print("Para o sálario informado no valor de R$",salario,"pagará o imposto de R$",imposto)
if base	< 1000:
	print("Para o sálario informado, não haverá pagamento do IR.")