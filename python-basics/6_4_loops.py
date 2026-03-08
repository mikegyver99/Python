"""
created on 2026-03-07 18:41:42
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# for n in range(2, 11):
#     print(n)

# n = 2
# while n >= 10:
#     print(n)
#     n += 1

def doubles(x):
    """ doubles the value"""
    double = x * 2
    return double
x = 4
for n in range(3):
    x = doubles(x)
    print(x)
    
