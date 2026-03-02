from __future__ import print_function

names = ["Ben", "Sally", "Amy", "George", "Randy", "Alice"]
print(names)

raw_newIndex = input('Please enter the index to replace:')
newIndex = int(raw_newIndex)

newName = input('Please enter the name to put into index:')

names[newIndex] = newName
print(names)

newName = input('Please enter the name to add to the list:')
names.append(newName)
print(names)

remName = input('Please enter the name to remove from the list:')
names.remove(remName)
print(names)