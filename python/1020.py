# Age in Days
# consider the whole year with 365 days and 30 days every month

def age_in_days(days):
    '''Converts value (days) to years, months and days'''
    age = {
        'years'  : 0,
        'months' : 0,
        'days'   : 0
        }
    while days:
        if days >= 365:
            age['years'] += 1
            days -= 365
        elif days >= 30:
            age['months'] += 1
            days -= 30
        elif days >= 1:
            age['days'] += 1
            days -= 1
    return age
    
days = int(input())
age = age_in_days(days)
print(
    '{} ano(s)\n'.format(age['years']) +
    '{} mes(es)\n'.format(age['months']) +
    '{} dia(s)'.format(age['days'])
    )
