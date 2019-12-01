# The Greatest

def higher_value(a, b, c):
  '''Calculates the greatest value'''
  ab = (a + b + abs(a - b)) / 2
  if ab > c:
    higher = ab
  else:
    higher = c
  return higher

#Read the input and split them into a list
numbers = input().split()

#Convert each list item to integers
a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

higher = int(higher_value(a, b, c))

print('{} eh o maior'.format(higher))
