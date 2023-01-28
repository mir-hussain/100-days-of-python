import random

print("Hangman")

word_list = ["Banana", "Apple", "Mango"]
life = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

selected_word = random.choice(word_list).lower()

print(selected_word)


blank_space = []

for letter in selected_word:
    blank_space.append("_")

print("".join(blank_space) + "\n")

while "_" in blank_space and life > 0:

    user_selection = input("Guess a letter: ").lower()

    if user_selection in selected_word:
        for i in range(0, len(selected_word)):
            if user_selection == selected_word[i]:
                blank_space[i] = user_selection
    else:
        life = life - 1

    print("".join(blank_space) + "\n")
    print(stages[life])

if life == 0:
    print("You lose.")

if not "_" in blank_space:
    print("You won.")
