import turtle
import pandas
from turtle import Screen

image = "bg.gif"

screen = Screen()
screen.title("Quiz")
screen.setup(width=700, height=500)
screen.addshape(image)
turtle.shape(image)


answer = screen.textinput(title="Guess the state",
                          prompt="What's another state name?")


turtle.mainloop()
