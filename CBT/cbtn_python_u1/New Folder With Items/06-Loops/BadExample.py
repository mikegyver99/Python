from __future__ import print_function

num = 5 #a number greater than 2 and less than 10
prime = True #a boolean to remember if this number is prime or not

if num % 2 == 0 and num != 2:
	print(num,'equals 2 *', num/2)
	prime = False

if num % 3 == 0 and num != 3:
	print(num,'equals 3 *', num/3)
	prime = False

if num % 4 == 0 and num != 4:
	print(num,'equals 4 *', num/4)
	prime = False

if num % 5 == 0 and num != 5:
	print(num,'equals 5 *', num/5)
	prime = False

if num % 6 == 0 and num != 6:
	print(num,'equals 6 *', num/6)
	prime = False

if num % 7 == 0 and num != 7:
	print(num,'equals 7 *', num/7)
	prime = False

if num % 8 == 0 and num != 8:
	print(num,'equals 8 *', num/8)
	prime = False

if num % 9 == 0 and num != 9:
	print(num,'equals 9 *', num/9)
	prime = False

if prime:
	print(num,'is a prime number!')
else:
	print(num,'is not a prime number')