class DrinkOrder:
    def __init__(self):
        self.drinks = []
    
    def addBeverage(self, beverage):
        self.drinks.append(beverage)

    def getTotalOrder(self):
        total_price = 0.00
        order_str = ""
        for beverage in self.drinks:
            total_price += beverage.getPrice()
            order_str += f"* {beverage.getInfo()}\n"


        return f"Order Items:\n{order_str}Total Price: ${total_price:.2f}"