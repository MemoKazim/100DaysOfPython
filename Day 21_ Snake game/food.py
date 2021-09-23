from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color(62,90,20)
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        ran_x = random.randint(-380, 380)
        ran_y = random.randint(-335,335)
        ran_x = int(ran_x // 20) * 20
        ran_y = int(ran_y // 20) * 20
        self.goto(ran_x, ran_y)