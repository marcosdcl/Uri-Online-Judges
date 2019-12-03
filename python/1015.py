# Distance Between Two Points

import math

def convert_float(x, y):
  '''Convert a string in floats'''
  x = float(x)
  y = float(y)
  return x, y

def distance(x1, x2, y1, y2):
  '''Calculates the distance between axes of two points'''
  distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
  return distance

x1, y1 = input().split()
x1, y1 = convert_float(x1, y1)
x2, y2 = input().split()
x2, y2 = convert_float(x2, y2)
distance = distance(x1, x2, y1, y2)
print('{:.4f}'.format(distance))
