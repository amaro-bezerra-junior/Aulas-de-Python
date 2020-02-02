import math

def e_hipotenusa(n):
    i = 1
    while(i <= n):
        x = 1
        while(x <= n):
            a = i
            b = x
            c = int(math.sqrt((a ** 2) + (b ** 2)))
            if (c > a) and (c > b) and (c < (a + b)):
                if ((a ** 2) + (b ** 2) == c ** 2):
                    if(c == n):
                        return c
            x = x +1
        i = i + 1

    return 0

def soma_hipotenusas(n):
    soma = 0
    anterior = 0
    i = 1
    for i in range(1, n + 1):
        resultado = e_hipotenusa(i)
        if(resultado > anterior):
            anterior = resultado
            soma = soma + resultado

    return soma