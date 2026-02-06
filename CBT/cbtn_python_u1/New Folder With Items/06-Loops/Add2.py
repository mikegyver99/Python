#Fibonacci rules!
from __future__ import print_function

sum = 0
add = 10

for x in range(1,add):
	print('The current sum is:',sum)
	print('How much would you like to add?', end='')
	raw_add = raw_input('(Type 0 to end program): ')
	add = int(raw_add)
	sum = sum + add
	x = 1
	if add == 0:
		break