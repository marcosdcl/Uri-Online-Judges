#Simple Sort

numbers = [int(number) for number in input().split()]
ascending_numbers = sorted(numbers)
for number in ascending_numbers:
	print(number)
print('')
for number in numbers:
	print(number)
