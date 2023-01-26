from colorama import init, Fore
init()

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input(
    "You are on a cross road, where do you wanna go? \nType 'left' or 'right' => ").lower()

if direction == "right":
    action = input(
        "You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across => ").lower()
    if action == "wait":
        door = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? => ").lower()
        if door == "red":
            print(Fore.RED + "It's a room full of fire. GAME OVER.")
        elif door == "blue":
            print(Fore.RED + "You enter a room of beasts. GAME OVER.")
        elif door == "yellow":
            print(Fore.GREEN + "You found the treasure! You Win!")
        else:
            print(Fore.RED + "You chose a door that doesn't exist. GAME OVER.")
    else:
        print(Fore.RED + "You were eaten by crocodile. GAME OVER.")

else:
    print(Fore.RED + "You fell into a hole. GAME OVER.")
