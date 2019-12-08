# Snack

def snacks(code):
    '''a table with specification and value of snacks'''
    table = [
        ('Cachorro Quente', 4.00),
        ('X-Salada', 4.50),
        ('X-Bacon', 5.00),
        ('Torrada simples', 2.00),
        ('Refrigerante', 1.50)
        ]
    x = code - 1
    return table[x][1]


code_amount = input().split()
code = int(code_amount[0])
amount = int(code_amount[1])
item = snacks(code)
total_to_pay = item * amount
print('Total: R$ {:.2f}'.format(total_to_pay))
