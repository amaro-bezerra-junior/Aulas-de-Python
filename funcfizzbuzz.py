def fizzbuzz(x):
	if x % 3 == 0 and x % 5 == 0:
		return "FizzBuzz"
	elif x % 5 == 0:
		return "Buzz"
	if x % 3 == 0:
		return "Fizz"
	else:
		return x