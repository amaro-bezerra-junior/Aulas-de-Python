print("***************Financiamento da Casa Própria - Prestação***************")

valor_imovel = float(input("Qual o valor do imóvel: "))#entrada do valor do imóvel.
entrada = float(input("Informe o valor da entrada, caso haja: "))#caso haja entrada.
taxa = float(input("Informe a taxa de juros a ser aplicada: "))#entrada da taxa de juros a ser aplicada.
salario = float(input("Informe o sálario: "))#entrada do sálario.
anos = int(input("Informe a quantidade de anos a pagar: "))#entrada do período em anos.

meses = (anos * 12)#converte anos em meses.
juros_x = ((taxa / 100) + 1) ** meses * (taxa / 100)#bloco 1
juros_y = ((taxa / 100) + 1) ** meses - 1#bloco 2
juros_principal = (juros_x / juros_y)#a divisão dos blocos 1 e 2 retornam o juros a ser aplicado no financiamento.
parcela = (valor_imovel - entrada) * juros_principal#retorna o valor da parcela.

porcentagem_salario = (salario * 0.3)#retorna o pertecentual do sálario informado.

if parcela <= porcentagem_salario:#compara o valor da parcela com o percentual do sálario.
	print(f"Financiamento autorizado. Valor da parcela R$ {parcela:6.2f}")
else:
	print(f"Financiamento não autorizado devido o valor da parcela ser maior que 30% do sálario. Valor da parcela R$ {parcela:6.2f}")
