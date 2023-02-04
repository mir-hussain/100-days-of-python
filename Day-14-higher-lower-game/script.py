from logo import logo, vs
from random import choice
from game_data import data
import os

score = 0
continue_game = True


def display_account_info(account_info):
    return f"{account_info['name']} is a {account_info['description']} from {account_info['country']}."


def check_answer(guess, account_a, account_b):
    if account_a["follower_count"] > account_b['follower_count']:
        return guess == 'a'
    else:
        return guess == 'b'


while continue_game:
    account_a = choice(data)
    account_b = choice(data)
    if account_a == account_b:
        account_b = choice(data)
    print(f"Current Score is {score}\n")
    print(f"Account A: {display_account_info(account_a)}")
    print(vs)
    print(f"Account B: {display_account_info(account_b)}")

    guess = input(
        "Which account has more follower? Type 'A' or 'B' : ").lower()

    result = check_answer(guess, account_a, account_b)

    if result:
        score += 1
        os.system("clear")
    else:
        os.system("clear")
        print(f"Wrong answer. Your total score is {score}")
        break
