<<<<<<< HEAD
print("Welcome to Black jack")
if input("Type 'y' to play, type 'n' to exit.") == "y":
    print("Game logic")
else:
    pass
=======
import random
import os
print("Blackjack")


def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_card(card_list):
    result = sum(card_list)
    distance = 21 - result

    return result, distance


def display_result(user_cards, user_score, computer_cards, computer_score, winner):
    print(
        f"Computer cards are {computer_cards}. Total Score is {computer_score}")
    print(f"User cards are {user_cards}. Total Score is {user_score}")
    if not winner:
        print("Draw")
    else:
        print(f"{winner} is the winner.")


def check_result(user_score, user_cards, user_distance,
                 computer_score, computer_cards, computer_distance):
    if user_score == computer_score:
        display_result(computer_score=computer_score,
                       computer_cards=computer_cards,
                       user_cards=user_cards,
                       user_score=user_score,
                       winner="")
    elif user_distance > computer_distance:
        display_result(computer_score=computer_score,
                       computer_cards=computer_cards,
                       user_cards=user_cards,
                       user_score=user_score,
                       winner="Computer")
    elif user_distance < computer_distance:
        display_result(computer_score=computer_score,
                       computer_cards=computer_cards,
                       user_cards=user_cards,
                       user_score=user_score,
                       winner="User")


def play_game():
    user_cards = []
    computer_cards = []

    for x in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score, user_distance = calculate_card(user_cards)
    computer_score, computer_distance = calculate_card(computer_cards)

    print(
        f"Your cards are {user_cards}, total score is {user_score}")

    print(f"Computer's first card is {computer_cards[0]}")

    if user_score > 21 and computer_score < 21:
        display_result(computer_score=computer_score,
                       computer_cards=computer_cards,
                       user_cards=user_cards,
                       user_score=user_score,
                       winner="Computer")
    elif user_score < 21 and computer_score > 21:
        display_result(computer_score=computer_score,
                       computer_cards=computer_cards,
                       user_cards=user_cards,
                       user_score=user_score,
                       winner="User")
    else:
        if input("Do you want to draw another card? Type 'y' or 'n': ") == "n":
            check_result(user_score, user_cards, user_distance,
                         computer_score, computer_cards, computer_distance)
        else:
            user_cards.append(deal_card())
            user_score, user_distance = calculate_card(user_cards)
            check_result(user_score, user_cards, user_distance,
                         computer_score, computer_cards, computer_distance)


while input("Do you wanna play a game of blackjack? type 'y' or 'n': ") == 'y':
    os.system("clear")
    play_game()
>>>>>>> 0c45f9cb54589089435902af5d30678dad40f0a2
