from turtle import Turtle

FONT = ('Courier' , 80 , 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_score()

    def update_score(self):
        ##RIGHT##
        self.goto(100, 200)
        self.write(self.r_score , False, 'center', FONT)
        ##LEFT##
        self.goto(-100, 200)
        self.write(self.l_score , False, 'center', FONT)

    def r_win(self):
        self.clear()
        self.r_score += 1
        self.update_score()
    
    def l_win(self):
        self.clear()
        self.l_score += 1
        self.update_score()