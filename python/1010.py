# Simple Calculate

def product_calc(qt, price):
  '''Calculates total price per product quantity'''
  calc = qt * price
  return calc

def product_tot(product_1, product_2):
  '''Sum of product 1 to 2'''
  total = product_1 + product_2
  return total

#Read the inputs and break them into a list
product_1 = input().split()
product_2 = input().split()

#Convert each list item to integers and float
id_1 = int(product_1[0])
qt_1 = int(product_1[1])
price_1 = float(product_1[2])
id_2 = int(product_2[0])
qt_2 = int(product_2[1])
price_2 = float(product_2[2])

#Calculates total price per product quantity
calc_1 = product_calc(qt_1, price_1)
calc_2 = product_calc(qt_2, price_2)

#Sum of product 1 to 2
total = product_tot(calc_1, calc_2)

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
