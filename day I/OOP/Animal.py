# Polymorphism

# Part 1
class Dog:
    def __init__(self):
        pass

    def intro(self):
        print("I am a dog")

    def makeSound(self):
        print("Woof!")


class Cat:
    def __init__(self):
        pass

    def intro(self):
        print("I am a cat")

    def makeSound(self):
        print("Meow!")


d = Dog()
d2 = Dog()
c = Cat()
c2 = Cat()

animals = [d, c, c2, d2]

for animal in animals:
    animal.intro()
    animal.makeSound()
    print()

# Part 2
class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print("I am an animal")

    def __str__(self):
        return "My name is " + self.name


class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def intro(self):
        print("I am a goat")

    def makeSound(self):
        print("Meh!")


class Cow(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def intro(self):
        print("I am a cow")

    def makeSound(self):
        print("Moo!")


a = Goat("Alpine")
b = Cow("Leo")

print(a)
a.intro()
a.makeSound()
print()

b.intro()
b.makeSound()
