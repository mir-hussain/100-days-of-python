from turtle import Turtle

MOVEMENT = 20


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.left(90)
        self.goto(self.xcor(), -180)

    def move_up(self):
        y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), y)
