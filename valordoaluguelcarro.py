print("**********Programa para calcular custo com aluguel de carro.**********")

km_rodados = float(input("Informe a quantida de km's rodados: "))
dias_rodados = int(input("Informe os dias de locação do veículo: "))
valor_aluguel_carro = float(input("Informe o valor referente ao aluguel do veículo: "))
valor_km_carro = float(input("Informe o valor do km rodado: "))

valor_km = (km_rodados * valor_km_carro)
valor_dia = (dias_rodados * valor_aluguel_carro)
total_locacao = (valor_km + valor_dia)

print("O valor do km rodado é R$",valor_km,"e o valor total da locação é de R$",valor_dia,"totalizando o valor de R$",total_locacao)