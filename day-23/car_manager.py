from random import random
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEEDS=[5,10,15,20]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager():
    def __init__(self):
        super().__init__()
        self.cars=[]
        self.spawn_cars(10)
        self.dx=1

    def spawn_cars(self,n):
        for i in range(n):
            turtle=Turtle()
            turtle.color(random.choice(COLORS))
            turtle.penup()
            turtle.shape("square")
            turtle.shapesize(stretch_wid=1, stretch_len=2)
            turtle.goto(280+random.randint(1,10)*20,random.randint(-10,10)*22)
            self.cars.append(turtle)

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor()-MOVE_INCREMENT-self.dx)

    def increase_speed(self):
        self.dx*=2





