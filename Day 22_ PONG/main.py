from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

DELAY = 0.05

screen = Screen()
screen.setup(800, 600)
screen.title('PONG')
screen.bgcolor('black')
screen.tracer(0)

player_1 = Paddle((350, 0))
player_2 = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(player_1.up, 'Up')
screen.onkeypress(player_1.down, 'Down')
screen.onkeypress(player_2.up, 'w')
screen.onkeypress(player_2.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(DELAY)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(player_1) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        DELAY *= 0.9
    
    if ball.distance(player_2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        DELAY *= 0.9

    ## L WIN
    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_win()
        DELAY = 0.05

    ## R WIN
    if ball.xcor() < -380:
        ball.reset_ball()
        score.r_win()
        DELAY = 0.05

screen.exitonclick()