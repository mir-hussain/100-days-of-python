import turtle
import pandas
from turtle import Screen
from label import Label


image = "bg.gif"
guess_list = []
screen = Screen()
screen.title(f"{len(guess_list)}/50")
screen.setup(width=700, height=500)
screen.addshape(image)
turtle.shape(image)

state_dict = {}
state_data = pandas.read_csv("50_states.csv").values
for state_info in state_data:
    state_dict[state_info[0]] = (state_info[1], state_info[2])

while len(guess_list) <= 50:

    answer = screen.textinput(title="Guess the state",
                              prompt="What's another state name?").title()
    if answer == "Exit":
        break

    if answer in state_dict and answer not in guess_list:
        label = Label(answer, state_dict[answer])
        guess_list.append(answer)
        screen.title(f"{len(guess_list)}/50")

missed_states = []

for state in state_dict:
    if state in guess_list:
        continue
    missed_states.append(state)

pandas.DataFrame({"State": missed_states}).to_csv("Missed.csv")
