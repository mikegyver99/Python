from helpers.string import shout
from helpers.math import area

length = 9
width = 5
message = f"The area of a {width}-by-{length} rectangle is {area(width, length)}"
print(shout(message))