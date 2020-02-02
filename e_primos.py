def ePrimo(x):
    fator = 2
    while fator * fator <= x:
        if x % fator == 0:
            return False
        fator += 1
    else:
        return True

def n_primos(n):

    lista_primos = 0
    for i in range(2, n + 1):
        if ePrimo(i):
            lista_primos += 1

    return lista_primos
