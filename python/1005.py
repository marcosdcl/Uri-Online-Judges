# Average 1

def pond_avr(a, b):
	pond = (a * 3.5) + (b * 7.5)
	avr = pond / 11
	return avr
	
A = float(input())
B = float(input())
media = pond_avr(A, B)
print('MEDIA = {:.5f}'.format(media))

