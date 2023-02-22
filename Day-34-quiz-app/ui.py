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
        self.canvas.pack()

        self.window.mainloop()
