import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_nato_alphabet():

    str = input("Enter your word: ").replace(" ", "").upper()
    try:
        alphabet_list = [alphabet for alphabet in str]
        nato_alphabet = [data_dict[alphabet] for alphabet in alphabet_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato_alphabet()
    else:
        print(nato_alphabet)


generate_nato_alphabet()
