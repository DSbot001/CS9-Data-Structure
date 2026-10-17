from Beverage import Beverage

class FruitJuice(Beverage):
    def __init__(self, ounces, price, fruits):
        super().__init__(ounces, price)
        self.fruits = fruits

    def getInfo(self):
        fruit_str = ""
        for fruit in self.fruits:
            fruit_str += fruit + "/"

        return f"{fruit_str[:-1]} Juice, {super().getInfo()}" 
