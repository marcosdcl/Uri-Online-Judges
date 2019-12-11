# Coordinates of a Point

def quadrant_xy(x, y):
	'''Determine which quadrant the point belongs.'''
	if x > 0 and y != 0:
		if y > 0:
			quadrant = 'Q1'
		else:
			quadrant = 'Q4'
	elif x < 0 and y != 0:
		if y > 0:
			quadrant = 'Q2'
		else:
			quadrant = 'Q3'
	elif x == 0 and y == 0:
		quadrant = 'Origem'
	elif x == 0 and y != 0:
		quadrant = 'Eixo Y'
	elif x != 0 and y == 0:
		quadrant = 'Eixo X'
	return quadrant

x_y = input().split()
x = float(x_y[0])
y = float(x_y[1])
quadrant = quadrant_xy(x, y)
print(quadrant)
