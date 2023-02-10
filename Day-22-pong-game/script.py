from turtle import Turtle, Screen
from paddle import Paddle
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()

screen.tracer(0)

paddle_right = Paddle()


# paddle = Turtle()
# paddle.color("white")
# paddle.shape('square')
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)


def paddle_up():
    y = paddle_right.ycor() + 20
    paddle_right.goto(paddle_right.xcor(), y)


def paddle_down():
    y = paddle_right.ycor() - 20
    paddle_right.goto(paddle_right.xcor(), y)


screen.onkey(paddle_up, "Up")
screen.onkey(paddle_down, "Down")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()
