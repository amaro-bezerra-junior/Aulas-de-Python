print("**********Programa que calcula o valor da multa por excesso de velocidade.**********")

velocidade = float(input("Qual a velocidade do veículo: "))

if velocidade > 80:
	excesso = velocidade - 80
	multa = (excesso * 5)
	print("Você foi multado por excesso de velocidade no valor de R$",multa)
if velocidade < 80:
	print("Não ouve aplicação de multa para a velocidade informada!")