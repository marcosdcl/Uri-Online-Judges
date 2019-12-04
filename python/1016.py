# Distance

def distance(speed):
  '''calculates the distance between two cars'''
  dist = speed * 2
  return dist

speed = int(input())
dist = distance(speed)
print('%i minutos' % dist)
