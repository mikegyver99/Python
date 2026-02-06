from __future__ import print_function

ages = {"Ben":35, "Joe": 37, "Sally":22, "Jeff":18}

x = ages.keys()
print(x[2])


for age in ages:
	print('The age of ',age,'is',ages[age])