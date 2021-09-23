from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('arial', 25, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 315)
        self.color(62,90,20)
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', move=False, align=ALIGNMENT, font=FONT)
