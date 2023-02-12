from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_movement = 10
        self.y_movement = 10

    def move(self):
        x = self.xcor() + self.x_movement
        y = self.ycor() + self.y_movement
        self.goto(x, y)

    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1

    def ball_reset(self):
        self.home()
