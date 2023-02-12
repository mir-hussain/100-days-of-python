import os

dirname = os.path.dirname(__file__)
names_file = os.path.join(dirname, "names.txt")
letter_file = os.path.join(dirname, "starting_letter.txt")
output_folder = os.path.join(dirname, "output/")

name_list = []

with open(names_file, "r") as file:
    names = file.readlines()
    for name in names:
        clean_name = name.replace("\n", "")
        name_list.append(clean_name)

with open(letter_file, "r") as file:
    letter = file.read()

    for name in name_list:
        personalized_letter = letter.replace("[name]", name)
        with open(f"{output_folder}letter-for-{name}.txt", "w") as file:
            file.write(personalized_letter)

print("Done")
