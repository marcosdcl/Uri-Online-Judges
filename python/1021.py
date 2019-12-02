# Banknotes and Coins

def decompose(value):
    '''Calculates the smallest possible number of notes and coins'''
    notes = {
        '100' : 0,
        '50'  : 0,
        '20'  : 0,
        '10'  : 0,
        '5'   : 0,
        '2'   : 0,
        '1r'  : 0,
        '50c' : 0,
        '25c' : 0,
        '10c' : 0,
        '5c'  : 0,
        '1c'  : 0
        }
    while value > 0:
        #notes
        if value >= 100:
            notes['100'] += 1
            value -= 100
        elif value >= 50:
            notes['50'] += 1
            value -= 50
        elif value >= 20:
            notes['20'] += 1
            value -= 20
        elif value >= 10:
            notes['10'] += 1
            value -= 10
        elif value >= 5:
            notes['5'] += 1
            value -= 5
        elif value >= 2:
            notes['2'] += 1
            value -= 2
        #coins
        elif value >= 1:
            notes['1r'] += 1
            value -= 1
        elif value >= 0.50:
            notes['50c'] += 1
            value -= 0.50
        elif value >= 0.25:
            notes['25c'] += 1
            value -= 0.25
        elif value >= 0.10:
            notes['10c'] += 1
            value -= 0.10
        elif value >= 0.05:
            notes['5c'] += 1
            value -= 0.05
        elif value >= 0.01:
            notes['1c'] += 1
            value -= 0.01
        else:
            break
    return notes

value = float(input())
value += 0.0001
banknotes = decompose(value)

print(
    'NOTAS:\n' +
    '{} nota(s) de R$ 100.00\n'.format(banknotes['100']) +
    '{} nota(s) de R$ 50.00\n'.format(banknotes['50']) +
    '{} nota(s) de R$ 20.00\n'.format(banknotes['20']) +
    '{} nota(s) de R$ 10.00\n'.format(banknotes['10']) +
    '{} nota(s) de R$ 5.00\n'.format(banknotes['5']) +
    '{} nota(s) de R$ 2.00\n'.format(banknotes['2']) +
    'MOEDAS:\n' +
    '{} moeda(s) de R$ 1.00 \n'.format(banknotes['1r']) +
    '{} moeda(s) de R$ 0.50\n'.format(banknotes['50c']) +
    '{} moeda(s) de R$ 0.25\n'.format(banknotes['25c']) +
    '{} moeda(s) de R$ 0.10\n'.format(banknotes['10c']) +
    '{} moeda(s) de R$ 0.05\n'.format(banknotes['5c']) +
    '{} moeda(s) de R$ 0.01'.format(banknotes['1c'])
    )
