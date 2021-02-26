from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the ract? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

starting_y = -140
starting_x = -230
turtles = []

for color in colors:
    turtle = Turtle(shape='turtle')
    turtle.color(color)
    turtle.penup()
    starting_y += 40
    turtle.goto(x=starting_x, y=starting_y)
    turtles.append(turtle)
 
if user_bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost... The {winning_color} turtle is the winner.")

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()