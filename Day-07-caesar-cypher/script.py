letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ignore_chars = ['0', '1', '2', '3', '4', '5', '6', '7',
#                 '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+']


def encrypt(text, shift_value):
    encrypted = []

    shift_value = shift_value % 26

    for letter in text:
        if letter not in letters:
            encrypted.append(letter)
        else:
            index = letters.index(letter)
            encrypted.append(letters[index + shift_value])

    return "".join(encrypted)


def decrypt(str, shift_value):
    decrypted = []

    shift_value = shift_value % 26

    for letter in str:

        if letter not in letters:
            decrypted.append(letter)
        else:
            index = letters.index(letter)
            decrypted.append(letters[index - shift_value])

    return "".join(decrypted)


def run():
    mode = input(
        "Do you want to encrypt or decrypt ? write 'encrypt' or 'decrypt' ")

    if mode == "encrypt" or mode == "decrypt":

        text = input(f"Enter message to {mode} >>> ").lower()
        shift = int(input("Shift amount, [in number] >>> "))

        if mode == "encrypt":
            return encrypt(text, shift)
        else:
            return decrypt(text, shift)
    else:
        return "Invalid Input"


print(run())
