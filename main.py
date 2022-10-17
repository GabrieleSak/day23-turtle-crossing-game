import time
from random import random, randrange, uniform
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = []

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car = CarManager()
    cars.append(new_car)
    for car in cars:
        car.move()

    if player.ycor() >= 285:
        print("valio")
        scoreboard.level_up()
        player.reset_position()

    for car in cars:
        if player.distance(car) < 25:
            game_is_on =False
            scoreboard.game_over()


screen.exitonclick()