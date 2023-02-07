# TODO  : Prompt user by asking "What would you like? (espresso/latte/cappuccino)"
# TODO  : Turn off the coffee machine by entering "off" to the prompt.
# TODO  : Print Report
# NOTE  : Starting => Water = 100ml, Milk = 50ml, Coffee = 76g, Money = $2.5
# TODO  : Check if resources are sufficient
# TODO  : Process Coin.
# NOTE  : quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# NOTE  : If money is not sufficient - Sorry that's not enough money. Money refunded.

from prettytable import PrettyTable

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


resources_table = PrettyTable()
resources_table.field_names = ["Water (ml)", "Milk (ml)", "Coffee (gm)"]

menu_table = PrettyTable()
menu_table.field_names = list(MENU.keys())
menu_table.add_row(["$1.5", "$2.5", "$3.0"])


should_run = True


while should_run:

    choice = input(
        f"What would you like? \n{menu_table} \nespresso/latte/cappuccino : ").lower()

    if (choice == "espresso" or choice == "latte" or choice == "cappuccino"):

        print(resources)

        coins = {
            'quarters': 0,
            'dimes': 0,
            'nickles': 0,
            'pennies': 0,
        }
        amount_list = []

        for coin in coins:
            coins[coin] = int(input(f"How many {coin}: "))

        # NOTE  : quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01

        for coin in coins:
            if coin == "quarters":
                amount_list.append(coins[coin] * 0.25)
            elif coin == "dimes":
                amount_list.append(coins[coin] * 0.10)
            elif coin == "nickles":
                amount_list.append(coins[coin] * 0.05)
            else:
                amount_list.append(coins[coin] * 0.01)

        total_amount = sum(amount_list)

        if total_amount < MENU[choice]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = total_amount - MENU[choice]['cost']
            resources['water'] = resources['water'] - \
                MENU[choice]["ingredients"]["water"] or 0
            resources['milk'] = resources['milk'] - \
                MENU[choice]["ingredients"]["milk"] or 0
            resources['coffee'] = resources['coffee'] - \
                MENU[choice]["ingredients"]["coffee"] or 0

            print(resources)

            print(f"Here is ${round(change, 2)} in change.")
            print(f"Your {choice} is ready.")

    elif (choice == "report"):
        resources_table.add_row(list(resources.values()))
        print(resources_table)
    elif (choice == "off"):
        should_run = False
    else:
        print("Invalid choice")
