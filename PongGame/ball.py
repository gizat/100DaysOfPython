from turtle import Turtle

STEP = 10

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()

    def move(self):
        new_x = self.xcor() + STEP
        new_y = self.ycor() + STEP
        self.goto(new_x, new_y)