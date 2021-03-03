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
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(turtle) < 20:
            game_is_on = False
        




# TODO: Detect when the turtle player collides with a car
# TODO: Detect when the turtle player has reached the top edge of the screen
# TODO: Create a scoreboard








screen.exitonclick()