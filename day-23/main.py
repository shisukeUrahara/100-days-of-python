import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    spawn_car=random.randint(1,100)
    if(spawn_car<30):
        car_manager.spawn_cars(1)

    car_manager.move_cars()
    # detecting player reaching end
    if(player.ycor()>260):
        player.reset_position()
        scoreboard.levelup()
        car_manager.increase_speed()

    #checking collision with all cars
    for car in car_manager.cars:
        if player.distance(car) < 30:  # try 25–40 depending on your car size
            scoreboard.game_over()
            game_is_on = False
            break

    screen.update()


screen.exitonclick()
