# Consumption

def avg_consumption(distance, fuel):
  '''Calculate a car's average consumption'''
  consumption = distance / fuel
  return consumption

distance = int(input())
fuel = float(input())
consumption = avg_consumption(distance, fuel)
print('{:.3f} km/l'.format(consumption))
