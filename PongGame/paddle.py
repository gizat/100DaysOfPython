from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LEN = 1
STEP = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('square')     
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - STEP
        self.goto(self.xcor(), new_y)