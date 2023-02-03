import random

print("Welcome to number guessing game.")
print("I am thinking of a number from 1 to 100.")


def play_game():
    game_mode = input("To choose difficulty type 'easy' pr 'hard': ")

    number = random.randint(0, 101)
    attempts = 0

    if game_mode == 'easy':
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts left.")
        guess = int(input("Make a guess: "))

        if guess == number:
            print("You have guessed the right number.")
            break
        else:
            if number > guess:
                print("Too low.")
            else:
                print("Too high.")
            attempts -= 1

    if attempts == 0:
        print(f"You lose. The number was {number}")


play_game()
