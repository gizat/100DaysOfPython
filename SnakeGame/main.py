from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

def create_segments(position):
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.speed(0)
    new_segment.goto(position)
    segments.append(new_segment)

segments = []

for i in range(3):
    create_segments(starting_positions[i])









screen.exitonclick()