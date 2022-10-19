from random import choice, randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        if randint(1, 2) == 2:
            new_car = Turtle("square")
            new_car.speed("slowest")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.goto(280, randint(-260, 260))
            new_car.setheading(180)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT

