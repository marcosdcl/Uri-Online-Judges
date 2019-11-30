# Area

def triangle(base, height):
  '''Calculates the area of the rectangled triangle'''
  area = (base * height) / 2
  return area

def circle(radius):
  '''Calculates the area of the radius's circle'''
  area = 3.14159 * (radius * radius)
  return area

def trapezium(base_a, base_b, height):
  '''Calculates the area of the trapezium'''
  area = (base_a + base_b) * height / 2
  return area

def square(side):
  '''Calculates the area of the square'''
  area = side * side
  return area

def rectangle(base, height):
  '''Calculates the area of the rectangle'''
  area = base * height
  return area

#Read the inputs and break them into a list
values = input().split()

#Convert each list item to floats
A = float(values[0])
B = float(values[1])
C = float(values[2])

triangle_ = triangle(A, C)
circle_ = circle(C)
trapezium_ = trapezium(A, B, C)
square_ = square(B)
rectangle_ = rectangle(A,B)

print('TRIANGULO: {:.3f}\n'.format(triangle_) +
      'CIRCULO: {:.3f}\n'.format(circle_) +
      'TRAPEZIO: {:.3f}\n'.format(trapezium_) +
      'QUADRADO: {:.3f}\n'.format(square_) +
      'RETANGULO: {:.3f}'.format(rectangle_))
