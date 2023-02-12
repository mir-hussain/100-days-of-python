from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()

screen.tracer(0)

paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()


screen.onkey(paddle_right.paddle_up, "Up")
screen.onkey(paddle_right.paddle_down, "Down")
screen.onkey(paddle_left.paddle_up, "w")
screen.onkey(paddle_left.paddle_down, "s")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_right) < 50 and ball.xcor() > 325 or ball.distance(paddle_left) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.ball_reset()
        ball.bounce_x()

    if ball.xcor() < -390:
        ball.ball_reset()
        ball.bounce_x()

screen.exitonclick()
