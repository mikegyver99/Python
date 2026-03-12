class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} barks: {sound}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"
        return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)

print(f"{miles.name}'s age is {miles.age}.")
print(miles.speak())
print(miles.speak("Grr"))

