from colorama import init, Fore
import random
from hangman_art import logo, stages
from word_list import word_list

init()

print(logo)
life = 6


selected_word = random.choice(word_list).lower()

blank_space = []

for letter in selected_word:
    blank_space.append("_")

print("".join(blank_space) + "\n")

while "_" in blank_space and life > 0:

    user_selection = input("Guess a letter: ").lower()

    if user_selection in blank_space:
        print("You already guessed this letter correctly.")
    elif user_selection in selected_word:
        for i in range(0, len(selected_word)):
            if user_selection == selected_word[i]:
                blank_space[i] = user_selection
    else:
        print(f"There is no {user_selection} in the word. You lost a life.")
        life = life - 1

    print("".join(blank_space) + "\n")
    print(stages[life])

if life == 0:
    print(Fore.RED + f"You lose. The word was '{selected_word}'")

if not "_" in blank_space:
    print(Fore.GREEN + "You won.")
