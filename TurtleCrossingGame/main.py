import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.tracer(0)

turtle = Player()
cars = CarManager()

screen.listen()
screen.onkey(turtle.up, 'Up')

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if counter%6 == 0:
        cars.add_car()
    
    cars.move()
    counter += 1



# TODO: Detect when the turtle player collides with a car
# TODO: Detect when the turtle player has reached the top edge of the screen
# TODO: Create a scoreboard








screen.exitonclick()