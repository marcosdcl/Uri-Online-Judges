# Multiples

def multiples(a, b):
	if a > b:
		if a % b == 0:
			message = 'Sao Multiplos'
		else:
			message = 'Nao sao Multiplos'
	elif b > a:
		if b % a == 0:
			message = 'Sao Multiplos'
		else:
			message = 'Nao sao Multiplos'
	return message

a, b = [int(x) for x in input().split()]
message = multiples(a, b)
print(message)
