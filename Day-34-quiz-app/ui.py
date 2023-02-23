from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quiz_text: QuizBrain):
        self.quiz = quiz_text
        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # * Score Card

        self.score = Canvas(width=100, height=50,
                            bg=THEME_COLOR, highlightthickness=0)
        self.score.create_text(50, 25, text="Score: ",
                               font=("Aria", 18, "normal"), anchor="center")
        self.score.grid(row=1, column=1, padx=0)

        # * Que Card

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)

        self.question = self.canvas.create_text(150, 125, width=280, text="Test ",
                                                anchor="center", font=("Arial", 20, "normal"))
        # self.canvas.create_rectangle(0, 0, 300, 250, fill="white")
        self.canvas.grid(row=2, column=1, columnspan=2, pady=20)

        # * False Button

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=false_button_image, command=self.false_pressed)

        self.false_button.grid(row=3, column=1, pady=20)

        # * True Button

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=true_button_image, command=self.true_pressed)

        self.true_button.grid(row=3, column=2, pady=20)

        self.next_que()

        self.window.mainloop()

    def next_que(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
