from turtle import Screen
from subject import MyTurtle

screen = Screen()
screen.setup(height=400, width=600)
screen.listen()
screen.tracer(0)

turtle = MyTurtle()

screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()
