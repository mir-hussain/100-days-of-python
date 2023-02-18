from tkinter import *
from tkinter import messagebox
import random
import json

BACKGROUND_COLOR = "white"


def save_to_file():
    web = web_input.get()
    un = username_entry.get()
    pw = password_entry.get()

    new_data = {
        web: {
            "username": un,
            "password": pw
        }
    }

    if len(web) == 0 or len(un) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Empty Field",
                               message="Every filed must be filled out.")
    else:

        try:
            with open("pass.json", "r") as file:
                data = json.load(file)
        except:
            with open("pass.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("pass.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            web_input.delete(0, END)
            password_entry.delete(0, END)


def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)

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

    password_entry.insert(0, random_password)


def search_pass():

    web = web_input.get()

    if len(web) == 0:
        messagebox.showinfo(title="Empty Input",
                            message="Please enter a website to search.")
    else:
        try:
            with open("pass.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(
                title="File missing", message="No record available")
        else:
            try:
                messagebox.showinfo(
                    title="Credentials", message=f"Username: {data[web]['username']}\nPassword:{data[web]['password']}")
            except KeyError:
                messagebox.showwarning(
                    title="Invalid Website", message="A record associated with this website dose not exist")


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=200, height=200,
                bg=BACKGROUND_COLOR, highlightthickness=0)

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=1, column=2)

# Website

web_label = Label(text="Website:", bg=BACKGROUND_COLOR)
web_label.grid(row=2, column=1,  sticky='nesw')

web_input = Entry(width=40,)
web_input.grid(row=2, column=2,  sticky='nesw', pady=10)

# Search

search_button = Button(text="Search", command=search_pass)
search_button.grid(row=2, column=3,  sticky='nesw', pady=10)

# Username / Email

username_label = Label(text="Username/Email:", bg=BACKGROUND_COLOR)
username_label.grid(row=3, column=1,  sticky='nesw', pady=6)

username_entry = Entry(width=40)
username_entry.insert(0, "mir.hm110@gmail.com")
username_entry.grid(row=3, column=2, columnspan=2,  sticky='nesw')

# Password

password_label = Label(text="Password:", bg=BACKGROUND_COLOR)
password_label.grid(row=4, column=1,  sticky='nesw')

password_entry = Entry(width=29)
password_entry.grid(row=4, column=2,  sticky='nesw', pady=10)

gen_button = Button(text="Generate", command=password_gen)
gen_button.grid(row=4, column=3,  sticky='nesw',  pady=10)

# Add

add_button = Button(text="Add", command=save_to_file)
add_button.grid(row=5, column=2, columnspan=2, sticky='nesw')

window.mainloop()
