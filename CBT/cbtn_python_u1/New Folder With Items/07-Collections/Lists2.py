from __future__ import print_function

names = ["Ben", "Sally", "Amy", "George", "Randy", "Alice"]

for index in range(0,len(names)):
	print(names[index],'is found at index:',index)

for name in names:
	print(name,'is found at index:', names.index(name))
