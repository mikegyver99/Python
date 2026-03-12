# Create Goldenretriever class that inherits from Dog class.

# class Dog():
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"
    
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
    
# class GoldenRetriever(Dog):
#     def speak(self, sound="Bark"):
#         return super().speak(sound)
    
# miles = GoldenRetriever("miles", 4)

# print(f"{miles.speak()}, species {miles.species}, age{miles.age}")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# inherit from Rectangle.. observer behavior
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

rectangle = Rectangle(2, 4)
print(rectangle.area()) # 8

square = Square(4)
print(square.area())  # 16

square.width = 5  # Modifies .width but not .length
print(square.area())  # 20