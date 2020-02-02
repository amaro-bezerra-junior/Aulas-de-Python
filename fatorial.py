def fatorial (n):
	fat = 1
	while n > 1:
			fat = fat * n
			n = n - 1
	return(fat)
    
def numero_binomial(n, k):
	return fatorial(n) / (fatorial(k) * fatorial(n - k))
