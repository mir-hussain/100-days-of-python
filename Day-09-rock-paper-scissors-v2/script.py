from random import randint
from random import shuffle
from colorama import init, Fore
init()

action_list = ["rock", "paper", "scissor"]


def random_action(input_list):
    index = randint(0, 2)
    shuffle(input_list)
    return input_list[index]


def get_user_input():
    user_input = input(
        "Enter a action: 'rock', 'paper', 'scissor' : ").lower()
    while not user_input in action_list:
        return get_user_input()
    return user_input


def show_result(computer_action, user_input, winning_msg):
    print(Fore.RESET + "_-_-_-_-_-_")
    print(f"Computer action, {computer_action}")
    print(f"User input, {user_input}")
    print(Fore.GREEN + winning_msg)
    print(Fore.RESET + "_-_-_-_-_-_\n")


def game():
    action = random_action(action_list)
    user_input = get_user_input()

    while action == user_input:
        print()
        print(Fore.RED + "!!!!!!!!!!!!!!")
        print(f"Computer action, {action}")
        print(f"User input, {user_input}")
        print('Same action, please try again')
        print("!!!!!!!!!!!!!!\n")
        print(Fore.RESET)
        return game()

    if user_input == "rock" and action == "scissor":
        show_result(action, user_input, "You Won")

    elif user_input == "scissor" and action == "rock":
        show_result(action, user_input, "Computer wins")

    elif user_input == "paper" and action == "rock":
        show_result(action, user_input, "You Won")

    elif user_input == "rock" and action == "paper":
        show_result(action, user_input, "Computer wins")

    elif user_input == "scissor" and action == "paper":
        show_result(action, user_input, "You Won")

    elif user_input == "paper" and action == "scissor":
        show_result(action, user_input, "Computer wins")


start = 1

while start == 1:
    game()

    print("1 => Try again")
    print("0 => Exit")
    start = int(input())
