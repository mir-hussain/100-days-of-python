# TODO  : Prompt user by asking "What would you like? (espresso/latte/cappuccino)"
# TODO  : Turn off the coffee machine by entering "off" to the prompt.
# TODO  : Print Report
# NOTE  : Starting => Water = 100ml, Milk = 50ml, Coffee = 76g, Money = $2.5
# TODO  : Check if resources are sufficient
# TODO  : Process Coin.
# NOTE  : quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
