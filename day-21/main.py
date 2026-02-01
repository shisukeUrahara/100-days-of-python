from symtable import Class
from turtle import Turtle,Screen
import time
import random

screen = Screen()
snake_segments=[]
segment_positions=[(0,0),(-20,0),(-40,0)]

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")

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
           self.add_segment(pos)
        self.head=self.segments[0]

    def add_segment(self,position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position[0],position[1])
        self.segments.append(t)

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

    def extend(self):
        self.add_segment(self.segments[-1].position())


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fast")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score {self.score}",False,"center",("Arial",24,"normal"))


    def increment_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score {self.score}",False,"center",("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",False,"center",("Arial",24,"normal"))




snake = Snake()
food = Food()
scoreboard = Scoreboard()

def game_loop():
    is_game_on = True
    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        if (snake.head.distance(food) < 15):
            food.refresh()
            scoreboard.increment_score()
            # extend snake
            snake.extend()

        # check collision with boundary
        if (snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
            is_game_on = False
            scoreboard.game_over()

        # check collision with tail
        for segment in snake.segments[1::]:
            if(segment.distance(snake.head)<10):
                is_game_on = False
                scoreboard.game_over()







# bind keys BEFORE starting loop
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_loop()
screen.exitonclick()





