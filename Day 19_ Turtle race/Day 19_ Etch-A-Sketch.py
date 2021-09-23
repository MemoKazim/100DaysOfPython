from turtle import Screen, Turtle, onkey, onkeypress, pendown, penup

t=Turtle()
screen = Screen()

screen.listen()

def up():
    t.fd(10)

def down():
    t.bk(10)

def left():
    t.left(5)

def right():
    t.right(5)

def clear():
    t.home()
    t.clear()
    t.setheading(0)

screen.onkeypress(key='Up', fun=up)
screen.onkeypress(key='Down', fun=down)
screen.onkeypress(key='Right', fun=right)
screen.onkeypress(key='Left', fun=left)
screen.onkey(key='c', fun=clear)

screen.exitonclick()