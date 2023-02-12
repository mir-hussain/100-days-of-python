from turtle import Turtle


FONT = ("Courier", 15, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-280, 160)
        self.hideturtle()
        self.level = 1
        self.write(f"Level: {self.level}", font=FONT)
