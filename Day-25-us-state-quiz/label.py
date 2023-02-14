from turtle import Turtle


class Label(Turtle):
    def __init__(self, title, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.write(title)
