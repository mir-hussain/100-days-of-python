from turtle import Turtle


class Label(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write("Good")
