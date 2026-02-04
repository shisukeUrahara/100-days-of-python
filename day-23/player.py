from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.speed('fastest')
        self.color('green')

    def move(self):
        self.penup()
        if(self.ycor()<FINISH_LINE_Y):
            self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.penup()
        self.goto(STARTING_POSITION)


