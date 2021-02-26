from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def turn_leftwise():
    timmy.left(10)

def turn_rightwise():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=turn_leftwise)
screen.onkey(key='d', fun=turn_rightwise)
screen.onkey(key='c', fun=clear)
screen.exitonclick()