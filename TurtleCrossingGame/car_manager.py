from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STRETCH_WID = 2
STRETCH_LEN = 1
STARTING_X = 300

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []


    def add_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.y_cor = self.random_pos()
        new_car.goto(STARTING_X, new_car.y_cor)
        self.cars.append(new_car)


    def random_pos(self):
        return random.randint(-250, 250)


    def move(self):
        for car in self.cars:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.y_cor)