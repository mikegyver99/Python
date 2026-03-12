# -*- coding: utf-8 -*-
"""
created on 2026-03-11 08:46:38
@author: michael garcia mikejgarcia@gmail.com
version 1.0
"""
# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name, age, coat_color):
#         self.name = name
#         self.age = age
#         self.coat_color = coat_color
#     def __str__(self):
#         return f"{name} is {age} years old"
#     def speak(self, sound):
#         return f"{name} says {sound}"

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def drive(self, miles):
        self.mileage = miles
car1 = Car("blue", 20_000)
car2 = Car("red", 30_000)
car3 = Car("green", 0)
print(f"The {car1.color} car has {car1.mileage:,} miles.")
print(f"The {car2.color} car has {car2.mileage:,} miles.")
print(f"The {car3.color} car has {car3.mileage:,} miles.")
car3.drive(100)
print(f"The {car3.color} car has {car3.mileage:,} miles.")


# class Dog:
#     species = "Canis familiaris"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method prints object mem addr print(buddy)
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # dunder method prints details print(buddy)
#     def __str__(self):
#         return f"{self.name} is {self.age} years old"

#     # Another Instance
#     def speak(self, sound):
#         return f"{self.name} says {sound}"