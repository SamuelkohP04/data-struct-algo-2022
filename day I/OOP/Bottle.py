# Abstraction

from abc import ABC, abstractmethod


class Bottle(ABC):
    @abstractmethod
    def volume(self):
        pass


class smallBottle(Bottle):
    def volume(self):
        print("500ml")


class bigBottle(Bottle):
    def volume(self):
        print("1000ml")


sBottle = smallBottle()
sBottle.volume()  # output: 500ml

bBottle = bigBottle()
bBottle.volume()  # output: 1000ml
