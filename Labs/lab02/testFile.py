from Beverage import Beverage
from Coffee import Coffee
from FruitJuice import FruitJuice
from DrinkOrder import DrinkOrder


def test_beverage():
    beverage = Beverage(12, 4.5)

    assert beverage.getOunces() == 12
    assert beverage.getPrice() == 4.5
    assert beverage.getInfo() == "12 oz, $4.50"


def test_beverage_updates():
    beverage = Beverage(12, 4.5)
    beverage.updateOunces(16)
    beverage.updatePrice(11.25)

    assert beverage.getOunces() == 16
    assert beverage.getPrice() == 11.25
    assert beverage.getInfo() == "16 oz, $11.25"


def test_coffee():
    coffee = Coffee(8, 10.0, "Espresso")

    assert isinstance(coffee, Beverage)
    assert coffee.style == "Espresso"
    assert coffee.getOunces() == 8
    assert coffee.getPrice() ==10.0
    assert coffee.getInfo() == "Espresso Coffee, 8 oz, $10.00"


def test_fruit_juice():
    juice = FruitJuice(16, 6.5, ["Apple", "Orange", "Watermelon"])

    assert isinstance(juice, Beverage)
    assert juice.fruits == ["Apple", "Orange", "Watermelon"]
    assert juice.getInfo() == "Apple/Orange/Watermelon Juice, 16 oz, $6.50"


def test_empty_order():
    order = DrinkOrder()

    assert order.drinks == []
    assert order.getTotalOrder() == "Order Items:\nTotal Price: $0.00"


def test_drink_order():
    coffee = Coffee(8, 10.0, "Espresso")
    juice = FruitJuice(16, 6.5, ["Apple", "Orange", "Watermelon"])
    order = DrinkOrder()

    order.addBeverage(coffee)
    order.addBeverage(juice)

    assert order.drinks == [coffee, juice]
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Espresso Coffee, 8 oz, $10.00\n"
        "* Apple/Orange/Watermelon Juice, 16 oz, $6.50\n"
        "Total Price: $16.50"
        )

def test_coffee_updates():
    coffee = Coffee(8, 3.0, "Americano")
    coffee.updateOunces(12)
    coffee.updatePrice(4.5)

    assert coffee.getOunces() == 12
    assert coffee.getPrice() == 4.5
    assert coffee.getInfo() == "Americano Coffee, 12 oz, $4.50"


def test_juice_updates():
    juice = FruitJuice(8, 2.0, ["Orange"])
    juice.updateOunces(16)
    juice.updatePrice(5.0)

    assert juice.getOunces() == 16
    assert juice.getPrice() == 5.0
    assert juice.getInfo() == "Orange Juice, 16 oz, $5.00"




def test_duplicate_beverages():
    order = DrinkOrder()
    juice = FruitJuice(12, 4.0, ["Apple"])
    order.addBeverage(juice)
    order.addBeverage(juice)

    assert order.drinks == [juice, juice]
    assert order.getTotalOrder() == (
        "Order Items:\n"
        "* Apple Juice, 12 oz, $4.00\n"
        "* Apple Juice, 12 oz, $4.00\n"
        "Total Price: $8.00"
    )


