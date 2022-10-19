import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    for _ in range(randint(0, 1)):
        car_manager.create_car()
    car_manager.move()

    if player.ycor() >= 285:
        print("valio")
        scoreboard.level_up()
        player.reset_position()
        car_manager.speed_up()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
