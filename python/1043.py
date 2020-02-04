# Triangle

def triangle(a, b, c):
	''' Verify if is possible to make a triangle '''
	if a + b > c and a + c > b and b + c > a:
		return True
	else:
		return False

def perimeter(a, b, c):
	''' Calculates the perimeter of a triangle '''
	return a + b + c

def trapezium_area(a, b, c):
	''' Calculates the area of a trapezium '''
	return ((a + b) * c) / 2

numbers = input().split()

a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])

is_triangle = triangle(a, b, c)

if is_triangle == True:
	print('Perimetro = {:.1f}'.format(perimeter(a, b, c)))
elif is_triangle == False:
	print('Area = {:.1f}'.format(trapezium_area(a, b, c)))
