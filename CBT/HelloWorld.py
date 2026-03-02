"""Example experimenting with variable assignment and prints.

Contains simple variable definitions and prints. The file
appears to be used for learning how assignments and print
statements work in Python.
"""

UserName = 'mgarcia'
FullName = 'Mike J Garcia'
print(UserName)
print(FullName)

Altname = UserName
IncorrectName = 'FullName'
NewName = UserName = FullName
NewName = "New Name" = FullName
print(NewName)
print(UserName)
