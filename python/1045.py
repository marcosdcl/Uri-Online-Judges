# Triangle Types

def triangle_type(a, b, c):
	''' Check the type of triangle that three numbers can make '''
	message = []
	if a >= b + c:
		message += ['NAO FORMA TRIANGULO']
		return message
	if (a*a) == (b*b) + (c*c):
		message += ['RETANGULO']
	if (a*a) > (b*b) + (c*c):
		message += ['OBTUSANGULO']
	if (a*a) < (b*b) + (c*c):
		message += ['ACUTANGULO']
	if a == b and a == c:
		message += ['EQUILATERO']
	if a == b != c or b == c != a or a == c != b:
		message += ['ISOSCELES']

	return message


numbers = [float(x) for x in input().split()]
numbers.sort(reverse=True)
a = numbers[0]
b = numbers[1]
c = numbers[2]

message = triangle_type(a, b, c)
if message[0] == 'NAO FORMA TRIANGULO':
	print(message[0])
else:
	for alert in message:
		print('TRIANGULO', alert)
