list1 = [3,5,8]
list2 = [2,4,9]

for value in range(3):
	answer = list1[value] + list2[value]
	print('{} + {} = {}'.format(list1[value], list2[value], answer))