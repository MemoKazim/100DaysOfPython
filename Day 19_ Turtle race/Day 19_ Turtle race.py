from turtle import Screen, Turtle, onkey, onkeypress, pendown, penup, width, window_height, window_width
import random

Start = False

screen = Screen()
screen.setup(width=600, height=500)
color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
user_input = screen.textinput('Race' , 'Which turtle gonna win?')
turtle_list = []

if user_input:
    Start = True

for i in range(6):
    t=Turtle(shape='turtle')
    t.penup()
    t.color(color[i])
    t.goto(x=-265 , y=125 - i*50)
    turtle_list.append(t)


while Start:
    for turtle in turtle_list:
        if turtle.xcor() > 280:
            Start=False
            winner_turtle = turtle.pencolor()
            if user_input == winner_turtle:
                print(f"You won! {winner_turtle} is winner")
                break
            else:
                print(f"You lost! {winner_turtle} is winner")
                break            

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()