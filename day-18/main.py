from random import randint
from turtle import Turtle,Screen
import random

my_turtle= Turtle()
screen = Screen()
screen.colormode(255)


# # gui logic header
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# for _ in range(4):
#     for _ in range(10):
#         my_turtle.forward(10)
#         my_turtle.pendown()
#         my_turtle.forward(10)
#         my_turtle.penup()
#
#     my_turtle.left(90)

my_turtle.pendown()

def make_shape(sides,side_length):
    my_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for side in range(sides):
        my_turtle.forward(side_length)
        my_turtle.left(int(360/sides))

# make_shape(3,100)
# make_shape(4,100)
# make_shape(5,100)
# make_shape(6,100)
# make_shape(7,100)
# make_shape(8,100)
# make_shape(9,100)
# make_shape(10,100)

# random walk
# def random_walk():
#     while True:
#         my_turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         my_turtle.width(10)
#         my_turtle.forward(100)
#         my_turtle.setheading(int(360/randint(1,5)))
#
# random_walk()

# making a spirograph
def random_color():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def spirograph(radius=100, gap=5):
    my_turtle.speed("fastest")
    # gap = degrees to turn each step (smaller gap => more circles)
    for _ in range(int(360 / gap)):
        my_turtle.pencolor(random_color())
        my_turtle.circle(radius)
        my_turtle.setheading(my_turtle.heading() + gap)

spirograph(radius=120, gap=5)


screen.exitonclick()