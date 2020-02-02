print("**********Tabuada Assistida de Multiplicação: informe o início o fim da operação**********")

n = int(input("Tabuada de: "))
inicio = int(input("Informe o início da operação: "))
fim = int(input("Informe o fim da operação: "))

x = inicio
y = fim

while x <= y:
	print(n,"*",x,"=",n * x)
	x = x + 1