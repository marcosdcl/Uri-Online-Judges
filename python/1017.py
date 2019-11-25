# Fuel Spent

def fuel_spent(time, speed):
    '''Calculates the fuel spent with a car that does 12 Km/L'''
    total = (time * speed) / 12
    return total

hours = int(input())
avr_speed = int(input())
amount_spent = fuel_spent(hours, avr_speed)
print('{:.3f}'.format(amount_spent))
