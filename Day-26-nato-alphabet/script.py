import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

str = input("Enter your word: ").replace(" ", "").upper()

alphabet_list = [alphabet for alphabet in str]

nato_alphabet = [data_dict[alphabet] for alphabet in alphabet_list]

print(nato_alphabet)
