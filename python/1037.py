# Interval

def interval(value):
    '''Read a float-point and print the following intervals the number belongs.'''
    #The symbol '(' represents greather than. For example:
    #[0,25] indicates numbers between 0 and 25.0000, including both.
    #(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.
    message = ''
    if value >= 0 and value <= 25:
        message = 'Intervalo [0,25]'
    elif value > 25 and value <= 50:
        message = 'Intervalo (25,50]'
    elif value > 50 and value <= 75:
        message = 'Intervalo (50,75]'
    elif value > 75 and value <= 100:
        message = 'Intervalo (75,100]'
    else:
        message = 'Fora de intervalo'
    return message



value = float(input())
interval = interval(value)

print(interval)
