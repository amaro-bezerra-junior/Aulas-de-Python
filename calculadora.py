print("**********Calculadora Python**********")

print("Digite 1 para realizar a operação de Adição")
print("Digite 2 para realizar a operação de Subtração")
print("Digite 3 para realizar a operação de Multiplicação")
print("Digite 4 para realizar a operação de Divisão")

operacao = int(input("Informe a numeração a ser realizada (1, 2, 3, 4): "))

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

if operacao == 1:
	operando = (num1 + num2)
elif operacao == 2:
	operando = (num1 - num2)
elif operacao == 3:
	operando = (num1 * num2)
elif operacao == 4:
	operando = (num1 / num2)
else:
	print("Categoria invalida, digite as categorias entre 1 e 4")
	operando = 0
print("O resultado da operação é: ",operando)