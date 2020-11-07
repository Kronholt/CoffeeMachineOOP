class Drink:
    name = ""
    ingredients = {
        "water": 50,
        "coffee": 0,
        "milk": 0,
    }
    cost = 0.0

    def __init__(self, name, water, coffee, milk, cost):
        self.name = name
        self.ingredients['water'] = water
        self.ingredients['coffee'] = coffee
        self.ingredients['milk'] = milk
        self.cost = cost
