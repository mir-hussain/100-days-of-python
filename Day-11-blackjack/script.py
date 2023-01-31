import random
print("Blackjack")


def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_card(card_list):
    return sum(card_list)


user_cards = []
computer_cards = []

for x in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_card(user_cards)

print(
    f"Your cards are {user_cards}, total score is {user_score}")
