def maior_primo(n):

    primos = []
    for i in range(n):
        x = 0
        for y in range(n):
            if i%(y + 1) == 0: 
                x += 1
        if x == 2:
            primos.append(i)

    return(max(primos))
