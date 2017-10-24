print('-'*67)
print('Sum Bot')
print('')
number = input('Description: Please tell me a number and I will add all of the numbers from 1 up to the number that you gave me. ')
number = int(number)
print('')
total = 0
for count in range(1,number):
	total = total + count
print(total)
