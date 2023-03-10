from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "white"


def save_to_file():
    web = web_input.get()
    un = username.get()
    pw = password.get()

    if len(web) == 0 or len(un) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Empty Field",
                               message="Every filed must be filled out.")
    else:
        is_ok = messagebox.askokcancel(
            title=web, message=f"The information you entered is:\nWebsite:{web}, Email:{un}, Password:{pw}")

        if is_ok:
            with open("pass.txt", "a") as file:
                file.write(f"{web} | {un} | {pw}\n")
                web_input.delete(0, END)
                password.delete(0, END)


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password.delete(0, END)

    password_letters_list = [random.choice(
        letters) for _ in range(0, random.randint(6, 10))]
    password_numbers_list = [random.choice(
        numbers) for _ in range(0, random.randint(4, 6))]
    password_symbol_list = [random.choice(
        symbols) for _ in range(0,  random.randint(4, 6)
                                )]

    password_character_list = password_letters_list + \
        password_numbers_list + password_symbol_list

    random.shuffle(password_character_list)

    random_password = "".join(password_character_list)
    print(random_password)

    password.insert(0, random_password)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=200, height=200,
                bg=BACKGROUND_COLOR, highlightthickness=0)

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=1, column=2)

# Website

web_label = Label(text="Website:", bg=BACKGROUND_COLOR, pady=10)
web_label.grid(row=2, column=1)

web_input = Entry(width=40,)
web_input.grid(row=2, column=2, columnspan=2)

# Username / Email

username_label = Label(text="Username/Email:", bg=BACKGROUND_COLOR, pady=10)
username_label.grid(row=3, column=1)

username = Entry(width=40)
username.insert(0, "mir.hm110@gmail.com")
username.grid(row=3, column=2, columnspan=2)

# Password

password_label = Label(text="Password:", bg=BACKGROUND_COLOR)
password_label.grid(row=4, column=1)

password = Entry(width=29)
password.grid(row=4, column=2)

gen_button = Button(text="Generate", command=password_gen)
gen_button.grid(row=4, column=3)

# Add

add_button = Button(text="Add", command=save_to_file)
add_button.grid(row=5, column=2, columnspan=2, sticky='nesw', pady=10)

window.mainloop()
