# Bhaskara's Formula

import math

def bhaskara(a, b, c):
    '''Calculates and prints the root of bhaskara's formula if the value is positive'''
    x=(b ** 2) - (4 * a * c)
    if x > 0 and a > 0 and b > 0 and c > 0:
        x = math.sqrt(x)
        x1 = (-b + x) / ( 2 * a)
        x2=(-b - x) / ( 2 * a)
        message = 'R1 = {:.5f}\n'.format(x1) + 'R2 = {:.5f}'.format(x2)
    else:
        message = 'Impossivel calcular'
        
    return message

numbers = input().split()
a = float(numbers[0])
b = float(numbers[1])
c = float(numbers[2])
result = bhaskara(a, b, c)

print(result)
