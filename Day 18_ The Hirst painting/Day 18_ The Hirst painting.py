from turtle import Turtle, Screen, colormode, getscreen, penup
import random

memo = Turtle()
screen = Screen()
memo.speed(0)
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r, g, b)
    return tup

memo.penup()
memo.goto(-screen.window_width()/2 + 30, -screen.window_height()/2 + 30)
memo.pendown()

for i in range(1, 11):
    for _ in range(10):
        memo.dot(40,random_color())
        memo.penup()
        memo.fd(80)
    memo.goto(-screen.window_width()/2 + 30, -screen.window_height()/2 + 30 + i*80)

screen.exitonclick()
