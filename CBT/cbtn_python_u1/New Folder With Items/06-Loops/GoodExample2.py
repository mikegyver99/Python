from __future__ import print_function

num = 17 #a number greater than 2 and less than 10

for test in range(2,num):

	if num % test == 0 and num != test:
		print(num,'equals',test, '*', num/test)
		print(num,'is not a prime number')
		break
else:
	print(num,'is a prime number!')
