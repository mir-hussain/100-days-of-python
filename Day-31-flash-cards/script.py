import pandas
import random
from tkinter import *
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Aria"
timer = None
words = None

data = pandas.read_csv("./data/french_words.csv")
word_set = {row.French: row.English for (index, row) in data.iterrows()}


def flip_card(count):
    if count > 0:
        global timer
        timer = window.after(1000, flip_card, count - 1)
    else:
        canvas.itemconfig(card_image, image=card_back)
        canvas.itemconfig(title, text="English", fill="white")
        canvas.itemconfig(word, text=words["English"], fill="white")


def set_random_word():
    global words

    random_word = random.choice(list(word_set.keys()))
    meaning = word_set[random_word]

    words = {
        "French": random_word,
        "English": meaning
    }

    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=random_word, fill="black")
    flip_card(3)


def handle_known_word():
    print(words)
    set_random_word()


def handle_unknown_word():
    print(words)
    set_random_word()


# Main Window
window = Tk()
window.title("Flash Cards")
window.minsize(width=600, height=600)
window.config(bg=BACKGROUND_COLOR, padx=100, pady=100)

# Canvas

# Card
canvas = Canvas(width=800, height=600,
                bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_image = canvas.create_image(400, 300, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT, 60, "italic"))

canvas.grid(row=1, column=1, columnspan=2)

# Cross button

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, command=handle_known_word)
cross_button.grid(row=2, column=1)

# Check button

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, command=handle_unknown_word)
check_button.grid(row=2, column=2)

set_random_word()

window.mainloop()
