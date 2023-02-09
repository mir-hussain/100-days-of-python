from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=400, width=500)
color_list = ["red", "green", "blue", "yellow", "purple", "orange"]

for index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(color_list[index])
    turtle.penup()
    turtle.goto(-230, -120 + index * 50)

screen.exitonclick()
