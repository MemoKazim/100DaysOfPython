from turtle import Turtle, Screen, colormode, forward
import random as r

timmy = Turtle()

timmy.speed(0)
timmy.width(10)

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

direction = [0, 90, 180, 270]

for _ in range(200):
    timmy.setheading(r.choice(direction))
    timmy.forward(25)
    timmy.color(random_color())



screen = Screen()
screen.exitonclick()

