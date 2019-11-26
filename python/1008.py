# Salary

def sal_month(worked_hour, salary_hour):
    """Calculates the month salary"""
    salary = worked_hour * salary_hour
    return salary

id_number = input()
w_hour = float(input())
per_hour = float(input())
salary = sal_month(w_hour, per_hour)

print('NUMBER = ' + id_number + '\n' +
      'SALARY = U$ {:.2f}'.format(salary))
