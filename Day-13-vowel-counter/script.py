vowels = {
    "A": 0,
    "E": 0,
    "I": 0,
    "O": 0,
    "U": 0
}


text = input("Enter a text to count the vowels.").upper()
character_count = len(text)

for alphabet in text:
    if alphabet in vowels:
        vowels[alphabet] += 1

for character in vowels:
    rate = (vowels[character] / character_count) * 100
    print(
        f"{character} count = {vowels[character]}, appearance rate = {round(rate)}%")
