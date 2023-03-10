from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.color("white")
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_position, 0)

    def paddle_up(self):
        y = self.ycor() + 20
        if self.ycor() < 240:
            self.goto(self.xcor(), y)

    def paddle_down(self):
        y = self.ycor() - 20
        if self.ycor() > -240:
            self.goto(self.xcor(), y)
