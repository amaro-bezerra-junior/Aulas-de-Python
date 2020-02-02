salario = float(input("Informe o seu salário: "))
aumento = float(input("Informe o aumento desejado: "))

valorDoAumento = (aumento/100)*salario
novoSalario = (salario+(salario*aumento/100))

print("O aumento desejado é de R$",valorDoAumento,"e o novo salário é de R$",novoSalario)