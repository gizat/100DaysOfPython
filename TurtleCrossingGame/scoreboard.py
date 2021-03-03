from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-280, 260)
        self.update_score()


    def increase_score(self):
        self.score += 1


    def update_score(self):
        self.clear()
        self.write(f'LEVEL: {self.score}', False, align='left', font=FONT)

    
    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align='center', font=FONT)
