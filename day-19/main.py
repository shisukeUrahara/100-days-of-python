#  etch a sketch
from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

MOVE_DISTANCE = 10

def move_forward():
    my_turtle.forward(MOVE_DISTANCE)

def move_backward():
    my_turtle.backward(MOVE_DISTANCE)

def turn_left():
    my_turtle.left(10)

def turn_right():
    my_turtle.right(10)

def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "space")

screen.exitonclick()


