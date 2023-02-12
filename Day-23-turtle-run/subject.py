from turtle import Turtle

MOVEMENT = 20
STARTING_POSITION = -180


class MyTurtle(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.penup()
        self.left(90)
        self.goto(self.xcor(), STARTING_POSITION)

    def move_up(self):
        y = self.ycor() + MOVEMENT
        self.goto(self.xcor(), y)

    def move_down(self):
        y = self.ycor() - MOVEMENT
        self.goto(self.xcor(), y)

    def set_to_start(self):
        self.goto(self.xcor(), STARTING_POSITION)
