import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_park = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def add_car(self):
        color_car = Turtle("square")
        color_car.color(random.choice(COLORS))
        color_car.penup()
        color_car.shapesize(stretch_wid=1, stretch_len=2)
        color_car.goto(250, random.randint(-250, 250))
        self.car_park.append(color_car)


    def move_car(self):
        for element in self.car_park:
            element.backward(self.car_speed)

    def next_level(self):
        self.car_speed += MOVE_INCREMENT
