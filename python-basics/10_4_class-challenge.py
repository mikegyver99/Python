class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def talk(self, sound):
        if sound is None:
            return f"{self.name} Hello, I do not talk"
        else:
            return f"{self.name} I say {sound}"
    def run(self, run):
        if run is None:
            return f"{self.name} I cannot run"
        else:
            return f"{self.name} I can run"
        
class Cow(Animal):
    def talk(self, sound="Mow Mow"):
        return f"{super().talk(sound)}"

class Worm(Animal):
    def talk(self, sound=None):
        return f"{super().talk(sound)}"
    def run(self, run=None):
        return f"{super().run(run)}"

class Dog(Animal):
    def run(self, run="yes"):
        return f"{self.name} I can run fast"
    def talk(self, sound="Bark Bark"):
        return f"{super().talk(sound)}"

bessie = Cow("Bessie", "black")
print(f"{bessie.talk()}")
crawly = Worm("Crawly", "brown")
print(f"{crawly.talk()}\n{crawly.run()}")
fido = Dog("Fido", "Blue")
print(f"{fido.run()}\n{fido.talk()}")