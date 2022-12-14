from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(300, randint(-250, 250))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
