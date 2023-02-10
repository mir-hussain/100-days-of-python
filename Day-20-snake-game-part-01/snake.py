from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for number in range(0, 3):
            pen = Turtle(shape="square")
            pen.penup()
            pen.color("white")
            pen.goto(-20 * number, 0)
            self.segments.append(pen)

    def move(self):
        for index in range((len(self.segments) - 1), 0, -1):
            x = self.segments[index - 1].xcor()
            y = self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def left(self):
        self.segments[0].setheading(180)

    def right(self):
        self.segments[0].setheading(0)
