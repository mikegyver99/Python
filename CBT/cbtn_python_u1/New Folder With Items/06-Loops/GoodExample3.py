from __future__ import print_function

num = 17
test = 2

while test < num:
	if num % test == 0 and num != test:
		print(num,'equals',test, '*', num/test)
		print(num,'is not a prime number')
		break
	test = test + 1
else:
	print(num,'is a prime number!')

