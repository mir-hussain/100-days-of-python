from tkinter import *

BACKGROUND_COLOR = "white"

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
username.grid(row=3, column=2, columnspan=2)

# Password

password_label = Label(text="Password:", bg=BACKGROUND_COLOR)
password_label.grid(row=4, column=1)

password = Entry(width=29)
password.grid(row=4, column=2)

gen_button = Button(text="Generate")
gen_button.grid(row=4, column=3)

# Add

add_button = Button(text="Add")
add_button.grid(row=5, column=2, columnspan=2, sticky='nesw', pady=10)

window.mainloop()
