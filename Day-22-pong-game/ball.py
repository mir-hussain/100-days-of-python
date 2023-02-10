from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 0.05
        self.y_movement = 0.05

    def move(self):
        x = self.xcor() + self.x_movement
        y = self.ycor() + self.y_movement
        self.goto(x, y)

    def bounce(self):
        self.x_movement *= -1
        self.y_movement *= -1
