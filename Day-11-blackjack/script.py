import random
print("Blackjack")


def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_card(card_list):
    result = sum(card_list)
    distance = 21 - result

    return result, distance


def display_result(cards, total_score, winner):
    print(f"{winner}")


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

# if input("Do you want to draw another card? Type 'y' or 'n'") == "n":
#     if user_score > 21 and computer_score < 21:

#     if user_distance > computer_distance:
#         print(
#             f"Computer cards are {computer_cards}. Total score is {computer_score}")
#         print("Computer Wins.")
#     else:
#         print("You won.")
