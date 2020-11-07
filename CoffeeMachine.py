class CoffeeMachine:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    profit = 0
    on = True


    def report(self):
        print(f"water: {self.resources['water']}ml")
        print(f"milk: {self.resources['milk']}")
        print(f"coffe: {self.resources['coffee']}")
        print(f"profit: {self.profit}")


    def is_resource_sufficient(self, drink):
        """checks whether the machine has sufficient resources to make drink"""
        for ingredient in self.resources:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True

    def make_coffee(self, drink):
        """Takes drink order and subtracts ingredient cost from the resources of the machine"""
        for ingredient in drink.ingredients:
            self.resources[ingredient] -= drink.ingredients[ingredient]
            self.profit += drink.cost

    def power_down(self):
        self.on = False

    def is_on(self):
        return self.on

