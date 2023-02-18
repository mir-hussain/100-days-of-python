from tkinter import *
from tkinter import messagebox


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Aria"

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
canvas.create_image(400, 300, image=card_front)
canvas.grid(row=1, column=1, columnspan=2)

# Card title

title = Label(text="Title", font=(FONT, 40, "italic"), bg="white")
title.place(x=400, y=150, anchor="center")

# Word

word = Label(text="Word", font=(FONT, 60, "bold"), bg="white")
word.place(x=400, y=263, anchor="center")


# Cross button

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image)
cross_button.grid(row=2, column=1)

# Check button

check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image)
check_button.grid(row=2, column=2)


window.mainloop()
