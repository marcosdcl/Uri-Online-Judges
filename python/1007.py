# Difference

def prod(a, b):
  """Calculate the product of two numbers"""
  x = a * b
  return x

A = int(input())
B = int(input())
C = int(input())
D = int(input())

product_1 = prod(A, B)
product_2 = prod(C, D)
dif = product_1 - product_2
print('DIFERENCA = ' + str(dif))
