# Banknotes

def banknotes(amount):
    '''Calculates the smallest possible number of banknotes'''
    notes = {
        '100' : 0,
        '50'  : 0,
        '20'  : 0,
        '10'  : 0,
        '5'   : 0,
        '2'   : 0,
        '1'   : 0
        }
    while amount > 0:
        if amount >= 100:
            amount -= 100
            notes['100'] += 1
        elif amount >= 50:
            amount -= 50
            notes['50'] += 1
        elif amount >= 20:
            amount -= 20
            notes['20'] += 1
        elif amount >= 10:
            amount -= 10
            notes['10'] += 1
        elif amount >= 5:
            amount -= 5
            notes['5'] += 1
        elif amount >= 2:
            amount -= 2
            notes['2'] += 1
        elif amount >= 1:
            amount -= 1
            notes['1'] += 1
    return notes

amount = int(input())
print(amount)
notes = banknotes(amount)
print(
    str(notes['100']) + ' nota(s) de R$ 100,00\n' +
    str(notes['50'])  + ' nota(s) de R$ 50,00\n' +
    str(notes['20'])  + ' nota(s) de R$ 20,00\n' +
    str(notes['10'])  + ' nota(s) de R$ 10,00\n' +
    str(notes['5'])   + ' nota(s) de R$ 5,00\n' +
    str(notes['2'])   + ' nota(s) de R$ 2,00\n' +
    str(notes['1'])   + ' nota(s) de R$ 1,00'
    )
