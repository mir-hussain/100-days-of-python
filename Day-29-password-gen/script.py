from tkinter import *

window = Tk()
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)

lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)

canvas.pack()


window.mainloop()
