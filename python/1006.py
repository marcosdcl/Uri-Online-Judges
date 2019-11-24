# Average 2

def pond_avr(a, b, c):
	pond = (a * 2) + (b * 3) + (c * 5)
	avr = pond / 10
	return avr
	
A = round(float(input()), 2)
B = round(float(input()), 2)
C = round(float(input()), 2)
media = pond_avr(A, B, C)
print('MEDIA = {:.1f}'.format(media))

