from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
UP='Up'
DOWN='Down'
LEFT='Left'
RIGHT='Right'
screen.tracer(0)

# creating a paddle
class Paddle(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xcor,ycor)
        self.showturtle()
        # self.pendown()

    def up(self):
        if(self.ycor()>220):
            return
        else:
            self.goto(self.xcor(), self.ycor() + 30)



    def down(self):
        if(self.ycor()<-220):
            return
        else:
            self.goto(self.xcor(), self.ycor() - 30)

class Ball(Turtle):
    def __init__(self,xcor,ycor):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape('circle')
        self.dx=10
        self.dy=10
        self.goto(xcor,ycor)
        self.move_speed=0.04

    def move(self):
        # move first
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce(self,bouncex,bouncey):
        # bounce off top/bottom
        if(bouncex):
            self.dx *= -1
            self.move_speed*=0.9

        if(bouncey):
            self.dy *= -1
            self.move_speed*=0.9

    def reset_ball(self):
        self.move_speed=0.04
        self.goto(0,0)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def increment_left_score(self):
        self.l_score+=1
        self.refresh_score()

    def increment_right_score(self):
        self.r_score+=1
        self.refresh_score()








paddle_1=Paddle(350,0)
paddle_2=Paddle(-350,0)
scoreboard=Scoreboard()

screen.listen()
# paddle 1 movement
screen.onkey(paddle_1.up,UP)
screen.onkey(paddle_1.down,DOWN)

# paddle 2 movement
screen.onkey(paddle_2.up,'w')
screen.onkey(paddle_2.down,'s')





ball= Ball(0,0)

def play_game():
    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        # checking collision up or down wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce(False,True)

        # bounce missed right paddle
        if ball.xcor() > 380:
            ball.reset_ball()
            ball.bounce(True,False)
            scoreboard.increment_left_score()

        if ball.xcor() < -380:
            ball.reset_ball()
            ball.bounce(True,False)
            scoreboard.increment_right_score()

         # detecting collision with right paddle
        if(ball.distance(paddle_1)<50 and ball.xcor()>330):
            ball.bounce(True,False)

        # detecting collision with left paddle
        if(ball.distance(paddle_2)<50 and ball.xcor()<-330):
            ball.bounce(True,False)


play_game()

screen.exitonclick()