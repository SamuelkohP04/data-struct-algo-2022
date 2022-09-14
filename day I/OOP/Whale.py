# Inheritance


class Whale:

    # Class attributes
    species = "mammals"

    def __init__(self, age, size):
        # Instance attributes
        self.age = age
        self.size = size

    def whoAmI(self):
        return "I am a Whale"

    def myAge(self):
        return "I am {} years old".format(self.age)

    def eating(self, food):
        return "Eating {} ...".format(food)


# instantiating a whale object
blu = Whale(9, 10)

print(blu.whoAmI())  # output: I am a Whale
print(blu.eating("fish"))  # output: Eating fish ...

# inheritance
# Creating a child class
class Humpback(Whale):
    def __init__(self, age, size):
        super().__init__(age, size)

    def whoAmI(self):
        return "I am a Humpback Whale"


# instantiating child objects
h = Humpback(5, 8)

print(h.whoAmI())  # output: I am a Humpback Whale
print(h.myAge())  # output: I am 5 years old


# Extra Examples

# class Orca(Whale):
#     def __init__(self, age, size):
#         super().__init__(age, size)

#     def whoAmI(self):
#         return "I am an Orca"


# o = Orca(3, 4)

# print(o.whoAmI())
# print(o.myAge())
