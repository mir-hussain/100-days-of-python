from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = -1
        self.color("white")
        self.update()

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center",
                   font=("Arial", 20, "normal"))
