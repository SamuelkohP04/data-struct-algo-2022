# Encapsulation


class Pizza:
    def __init__(self):
        self.__price = 10

    def checkPrice(self):
        print("This pizza costs: ${}".format(self.__price))

    def changePrice(self, price):
        self.__price = price


p = Pizza()
p.checkPrice()  # output: This pizza costs: $10

# change the price of pizza without using the class's method
p.__price = 9
p.checkPrice()  # output: This pizza costs: $10

# change the price of pizza without using the method
p.changePrice(9)
p.checkPrice()  # output: This pizza costs: $9
