print("********** Saiba aqui o valor pela arrumação do guarda-roupa. **********")

camisa = int(input("Informe a quantidade de camisas: "))
calca = int(input("Informe a quantidade de calças: "))
bermuda = int(input("Informe a quantidade de bermudas: "))
cueca = int(input("Informe a quantidade de cuecas: "))
meia = int(input("Informe a quantidade de meias: "))

valor_camisa = camisa * 0.60
valor_calca = calca * 0.50
valor_bermuda = bermuda * 0.40
valor_cueca = cueca * 0.10
valor_meia = meia * 0.15

valor_total = (valor_camisa + valor_calca + valor_bermuda + valor_cueca + valor_meia)
print("Agradecemos os seus serviços. Você receberá o valor de R$",round(valor_total))

pagamento = int(input("Escolha uma forma de recebimento sendo 1 para pagamento em dinheiro e 2 para transferência: "))
forma_de_pagamento = pagamento

if forma_de_pagamento == 1:
	data = int(input("Informe a data da arrumação (dia em número ex: 1 ou 10...): "))
	data_pgto = data + 5
	if data_pgto >= 30:
		print("O valor de R$",round(valor_total),"será pago no próximo dia 01.")
	else:
		print("O valor de R$",round(valor_total),"será pago em",data_pgto)
if forma_de_pagamento == 2:
	agencia = input("Informe a sua agência: ")
	conta = input("Informe sua conta: ")
	data = int(input("Informe a data da arrumação (dia em número ex: 1 ou 10...): "))
	data_pgto = data + 3
	if data_pgto >= 30:
		print("Obrigado pelas informações. O valor será creditado em sua conta no próximo dia 01.")
	else:
		print("Obrigado pelas informações. O valor será creditado em sua conta em",data_pgto)
