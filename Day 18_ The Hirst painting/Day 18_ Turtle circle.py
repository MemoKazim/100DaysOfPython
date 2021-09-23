from turtle import Turtle, Screen, colormode, forward
import random as r
import turtle

timmy = Turtle()

timmy.speed('fastest')

def random_color():
    red = r.random()
    green = r.random()
    blue = r.random()
    rgb = []
    rgb.append(red)
    rgb.append(green)
    rgb.append(blue)
    rgb= tuple(rgb)
    return rgb


for _ in range(360//5):
    timmy.circle(150)
    timmy.color(random_color())
    timmy.rt(5)  



screen = Screen()
screen.exitonclick()

