import turtle
import pandas
from turtle import Screen
from label import Label

image = "bg.gif"

screen = Screen()
screen.title("Quiz")
screen.setup(width=700, height=500)
screen.addshape(image)
turtle.shape(image)

state_dict = {}
state_data = pandas.read_csv("50_states.csv").values
for state_info in state_data:
    state_dict[state_info[0]] = (state_info[1], state_info[2])

label = Label()

answer = screen.textinput(title="Guess the state",
                          prompt="What's another state name?")

if answer in state_dict:
    print("Good")
else:
    print("Not good")


turtle.mainloop()
