from __future__ import print_function

name = raw_input('Please tell me your name: ')
rawAge = input('Please tell me your age: ')
age = int(rawAge)

if age >= 21:
  print(name, 'You are older than 20 years old! You may enter.')
  print('What would you like to drink?')
elif age >=18:
  print('You are allowed in but not allowed to drink.')
  print('Feel free to dance')
else:
    print('Unfortunately',name,'you are younger then 18 and cannot enter.')

