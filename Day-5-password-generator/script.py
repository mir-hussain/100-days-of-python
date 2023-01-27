import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?: "))
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

password_list = []

if nr_letters != 0:
    for x in range(0, nr_letters):
        password_list.append(random.choice(letters))

if nr_symbols != 0:
    for x in range(0, nr_symbols):
        password_list.append(random.choice(symbols))

if nr_numbers != 0:
    for x in range(0, nr_numbers):
        password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = "".join(password_list)

print(f"Generated password is =>  {password}")
