from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LEN = 1
STEP = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.paddle = Turtle('square')        
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.goto(position)
        self.paddle.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)

    def up(self):
        new_y = self.paddle.ycor() + STEP
        self.paddle.goto(self.paddle.xcor(), new_y)
    

    def down(self):
        new_y = self.paddle.ycor() - STEP
        self.paddle.goto(self.paddle.xcor(), new_y)