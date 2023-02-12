import colorgram
import turtle
import random

turtle.colormode(255)

# NOTE : to get the colors from image
# image = "/home/mir/Projects/python/100-days-of-python/Day-17-spot-painting/image.jpg"

# def extract_color(image, color_number):
#     colors = colorgram.extract(image, color_number)
#     color_list = []
#     for color in colors:
#         r = color.rgb[0]
#         g = color.rgb[1]
#         b = color.rgb[2]
#         color_list.append((r, g, b))

#     return color_list

pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(750, 700)

pen.hideturtle()


def set_pen_position(x, y):
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()


def draw_dotted_line(dot_count):
    for _ in range(dot_count):
        pen.dot(20, random.choice(color_list))
        pen.penup()
        pen.forward(50)
        pen.pendown()
        pen.dot(20, random.choice(color_list))


set_pen_position(-250, -250)

color_list = [(186, 99, 30), (252, 46, 98), (27, 149, 50), (8, 183, 226), (22, 189, 116), (230, 167, 4), (251, 225, 54),
              (252, 57, 31), (117, 95, 193), (167, 57, 98), (1, 66, 139), (28, 134, 199), (249, 232, 238), (195, 146, 219)]


for i in range(1, 11):
    draw_dotted_line(10)
    set_pen_position(-250, -250 + (i * 50))

pen.hideturtle()

screen.exitonclick()
