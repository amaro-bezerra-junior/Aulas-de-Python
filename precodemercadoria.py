print("**********Informe o valor da mercadoria e o percentual de desconto**********")

valorDaMercadoria = float(input("Informe o valor da mercadoria: "))
desconto = float(input("Informe o valor do desconto a ser aplicado: "))

porcentagem = (desconto/100)
valorDoDesconto = (valorDaMercadoria * porcentagem)
valorFinal = valorDaMercadoria-(porcentagem * valorDaMercadoria)

print("O valor do desconto é R$",valorDoDesconto,"e o valor da mercadoria com desconto é de R$",valorFinal)