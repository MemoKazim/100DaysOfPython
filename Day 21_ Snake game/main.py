from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 700


screen = Screen()
screen.colormode(255)
screen.setup(WIDTH, HEIGHT)
screen.bgcolor(165,217,36)
screen.title('Snake Game')
screen.tracer(0)

user_input = screen.textinput('DIFFICULTY' , 'Choose your difficulty. (easy/hard)').lower()

SPEED = 0.05

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_mode = True
while game_mode:
    screen.update()
    time.sleep(SPEED)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    if user_input == 'easy':
        if snake.head.xcor() < -395:
            snake.head.goto(395, snake.head.ycor())
        elif snake.head.xcor() > 395:
            snake.head.goto(-395, snake.head.ycor())
        elif snake.head.ycor() < -350:
            snake.head.goto(snake.head.xcor(), 350)
        elif snake.head.ycor() > 350:
            snake.head.goto(snake.head.xcor(), -350)

        for segments in snake.body[1:]:
            if snake.head.distance(segments) < 15:
                game_mode = False
                score.game_over()

    elif user_input == 'hard':
        if snake.head.xcor() < -395 or snake.head.xcor() > 395 or snake.head.ycor() < -350 or snake.head.ycor() > 350:
            game_mode = False
            score.game_over()

        for segments in snake.body[1:]:
            if snake.head.distance(segments) < 15:
                game_mode = False
                score.game_over()
    
    else:
        print(f'unexpected input: {user_input}')
        game_mode = False

screen.exitonclick()