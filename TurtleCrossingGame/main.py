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

screen.listen()
screen.onkey(turtle.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# TODO: Create cars that are 20px high by 40px wide 
# TODO: Detect when the turtle player collides with a car
# TODO: Detect when the turtle player has reached the top edge of the screen
# TODO: Create a scoreboard








screen.exitonclick()