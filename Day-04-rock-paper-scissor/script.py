import random

rock = '''

Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''

Paper

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''

Scissors

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

computer_selection = random.randint(0, 2)

user_selection = int(input(
    "What do you choose? select '0' for rock, '1' for paper and '2' for scissors. : "))

print(f"Computer chose => \n {options[computer_selection]}")
print()
print(f"You chose => \n {options[user_selection]}")

if user_selection > 2 or user_selection < 0:
    print("Invalid input")
else:
    if user_selection == computer_selection:
        print("Draw")
    elif user_selection == 0 and computer_selection == 1:
        print("You lose.")
    elif user_selection == 1 and computer_selection == 0:
        print("You won.")
    elif user_selection == 1 and computer_selection == 2:
        print("You lose.")
    elif user_selection == 2 and computer_selection == 1:
        print("You won.")
    elif user_selection == 2 and computer_selection == 0:
        print("You lose.")
    elif user_selection == 0 and computer_selection == 2:
        print("You won.")
