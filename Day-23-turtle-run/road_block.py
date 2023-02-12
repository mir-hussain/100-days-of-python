from turtle import Turtle

MOVEMENT = 0.5


class Block(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.goto(position)

    def movement(self):
        x = self.xcor() - MOVEMENT
        self.goto(x, self.ycor())

    def reset_position(self):
        pass
