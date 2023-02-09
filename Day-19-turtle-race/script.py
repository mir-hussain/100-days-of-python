from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(height=400, width=500)
color_list = ["red", "green", "blue", "yellow", "purple", "orange"]
all_turtle = []

is_race_on = False

bet = screen.textinput(title="Make your bet.", prompt="Enter color")
print(bet)
for index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(color_list[index])
    turtle.penup()
    turtle.goto(-230, -120 + index * 50)
    all_turtle.append(turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        speed = randint(0, 30)
        turtle.forward(speed)

screen.exitonclick()
