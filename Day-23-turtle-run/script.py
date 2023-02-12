from turtle import Screen
from subject import MyTurtle
from score_board import Level

screen = Screen()
screen.setup(height=400, width=600)
screen.listen()
screen.tracer(0)

turtle = MyTurtle()

level = Level()

screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

game_on = True
while game_on:
    screen.update()

    if turtle.ycor() > 190:
        turtle.set_to_start()


screen.exitonclick()
