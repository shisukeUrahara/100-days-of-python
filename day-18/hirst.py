from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

t = Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()

color_list = [
    (215, 241, 229), (237, 207, 96), (109, 171, 203), (203, 228, 240),
    (245, 220, 230), (116, 191, 160), (38, 109, 150), (155, 60, 93)
]

DOT_SIZE = 20
SPACING = 60
ROWS = 5
COLS = 5

start_x = - (COLS - 1) * SPACING / 2
start_y = - (ROWS - 1) * SPACING / 2

for row in range(ROWS):
    for col in range(COLS):
        x = start_x + col * SPACING
        y = start_y + row * SPACING
        t.goto(x, y)
        t.dot(DOT_SIZE, random.choice(color_list))

screen.exitonclick()
