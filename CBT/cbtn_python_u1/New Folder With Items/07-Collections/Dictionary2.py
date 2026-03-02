from __future__ import print_function

ages = {"Ben":35, "Joe": 37, "Sally":22, "Jeff":18}
print(ages)

newKey = input("Please enter the key to change:")
raw_newVal = input("Please enter the value to change:")
newVal = int(raw_newVal)

ages[newKey] = newVal
print(ages)

newKey = input("Please enter a new key to add:")
raw_newVal = input("Please enter a new value to add:")
newVal = int(raw_newVal)

ages[newKey] = newVal
print(ages)

remKey = input("Please tner a key to remove:")

del ages[remKey]
print(ages)