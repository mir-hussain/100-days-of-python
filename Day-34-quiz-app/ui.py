from tkinter import *


THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)

        self.canvas.create_text(150, 125, text="Test ",
                                anchor="center", font=("Arial", 20, "normal"))
        # self.canvas.create_rectangle(0, 0, 300, 250, fill="white")
        self.canvas.grid(row=1, column=1, columnspan=2, pady=20)

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image)

        self.false_button.grid(row=2, column=1, pady=20)

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image)

        self.true_button.grid(row=2, column=2, pady=20)

        self.window.mainloop()
