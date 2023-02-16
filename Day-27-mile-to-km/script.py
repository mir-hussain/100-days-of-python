from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

user_input = Entry()
user_input.grid(column=2, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)

equal_label = Label(text="is equal to")
equal_label.grid(column=1, row=2)

km_number = Label(text="0")
km_number.grid(column=2, row=2)

km_label = Label(text="Km")
km_label.grid(column=3, row=2)

calculate_button = Button(text="Calculate")
calculate_button.grid(column=2, row=3)

window.mainloop()
