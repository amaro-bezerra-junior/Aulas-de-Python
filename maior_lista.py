def maior_elemento(lista):
	numero = lista[0]
	i = 1
	while i < len(lista):
		if lista[i] > numero:
			numero = lista[i]
		i = i + 1
	return numero