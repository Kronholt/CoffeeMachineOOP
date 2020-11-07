from CoffeeMachine import CoffeeMachine
from Drink import Drink

espresso = Drink("espresso", 50, 18, 0, 1.5)
latte = Drink("latte", 200, 24, 150, 2.5)
cappuccino = Drink("cappuccino", 250, 100, 24, 3.8)


machine = CoffeeMachine()

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * .25
    total += int(input("how many dimes?: ")) * .10
    total += int(input("how many nickels?:")) * .05
    total += int(input("how many pennies?:")) * .01
    return total

while machine.is_on():
    choice = input("What would you like to drink (espresso/latte/cappuccino): ")
    if choice == "off":
        machine.power_down()
    elif choice == "report":
        machine.report()
    else:
        if choice == "espresso":
            drink = espresso
        elif choice == "latte":
            drink = latte
        elif choice == "cappuccino":
            drink = cappuccino
        else:
            print("Incorrect choice")
            continue
        if machine.is_resource_sufficient(drink):
            coins = process_coins()
            if coins >= drink.cost:
                print(f"Your change is ${round(coins - drink.cost,2)}")
                machine.make_coffee(drink)




