from symtable import Class
from turtle import Turtle,Screen
import time

screen = Screen()
snake_segments=[]
segment_positions=[(0,0),(-20,0),(-40,0)]

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
x_coordinate=0
y_coordinate=0

# def init_turtle():
#     for i in range(3):
#         turtle = Turtle()
#         turtle.penup()
#         turtle.color("white")
#         turtle.shape("square")
#         turtle.goto(segment_positions[i][0],segment_positions[i][1])
#         snake_segments.append(turtle)
#
# def start_moving():
#     is_game_on=True
#     while is_game_on:
#         screen.update()
#         time.sleep(0.1)
#         for segment_index in range(len(snake_segments)-1,0,-1):
#             segment=snake_segments[segment_index]
#             segment.penup()
#             segment.speed("slowest")
#             new_x=snake_segments[segment_index-1].xcor()
#             new_y=snake_segments[segment_index-1].ycor()
#             segment.goto(new_x,new_y)
#             segment.pendown()
#         snake_segments[0].forward(20)
#
#
#
# def start_game():
#     screen.tracer(0)
#     init_turtle()
#     screen.update()
#     start_moving()
#     screen.exitonclick()
#
# start_game()

# oops version
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in positions:
            t = Turtle("square")
            t.color("white")
            t.penup()
            t.goto(pos)
            self.segments.append(t)
        self.head=self.segments[0]

    def move(self):
        # move tail -> head
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

snake = Snake()

def game_loop():
    snake.move()
    screen.update()
    screen.ontimer(game_loop, 100)  # call again in 100ms

# bind keys BEFORE starting loop
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_loop()
screen.exitonclick()





