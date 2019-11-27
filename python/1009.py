# Salary with Bonus

def commission(salary, sales):
  '''Calculate the commission of the seller'''
  commission = sales * 0.15
  total = salary + commission
  return total

seller = input()
salary = float(input())
sales = float(input())
total = commission(salary, sales)

print('TOTAL = R$ {:.2f}'.format(total))
