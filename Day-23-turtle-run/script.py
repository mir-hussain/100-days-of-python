from turtle import Screen
from subject import MyTurtle
from score_board import Level
from road_block import Block
from random import randint
from time import sleep

screen = Screen()
screen.setup(height=400, width=600)
screen.listen()
screen.tracer(0)

blocks = []

turtle = MyTurtle()
level = Level()

# block = Block((90, 150))
# block.movement()

list = ["red", "green", "blue"]

for _ in range(0, 25):

    random_x = randint(-280, 280)
    random_y = randint(-180, 180)
    block = Block((random_x, random_y), list[randint(0, 2)])
    blocks.append(block)


screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

game_on = True
while game_on:
    screen.update()

    for block in blocks:
        if block.xcor() < -310:
            block.goto(310, block.ycor())

        block.movement()

    if turtle.ycor() > 190:
        turtle.set_to_start()
        level.update()


screen.exitonclick()
