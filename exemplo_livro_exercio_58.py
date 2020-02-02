p = int(input("Primeiro número: "))
s = int(input("Segundo número: "))
x = 1
r = 0

while x <= s:
	r = r + p
	x = x + 1
print("%d x %d = %d" % (p,s,r))