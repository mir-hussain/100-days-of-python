import os

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')
print("Welcome to secret auction.")

participants = {}

should_run = True


def find_highest_bidder(data):
    highest_bid = 0
    winner = ""

    for name in data:
        bid = data[name]
        if bid > highest_bid:
            highest_bid = bid
            winner = name

    print(f"The winner is {winner}, with the amount of {highest_bid}$")


while should_run:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid amount: "))
    participants[name] = bid
    choice = input(
        "Is there anyone else ? type 'yes' and handover, or type 'no' to exit. : ")

    if choice == "no":
        find_highest_bidder(participants)
        should_run = False
    elif choice == "yes":
        os.system('cls||clear')
    else:
        print("Invalid Input")
        should_run = False
