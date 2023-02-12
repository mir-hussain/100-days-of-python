from turtle import Turtle
from random import randint

MOVEMENT = 0.1


class Block(Turtle):
    def __init__(self,  color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.random_x = randint(-280, 280)
        self.random_y = randint(-120, 180)
        self.goto(self.random_x, self.random_y)

    def movement(self):
        x = self.xcor() - MOVEMENT
        self.goto(x, self.ycor())
