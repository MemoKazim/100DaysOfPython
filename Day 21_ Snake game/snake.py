from turtle import Turtle, Screen, setheading

TURTLE_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in TURTLE_POSITION:
            self.add_part(position)
    
    def add_part(self, position):
        new_part = Turtle('square')
        new_part.penup()
        new_part.color(62,90,20)
        new_part.goto(position)
        self.body.append(new_part)

    def extend_snake(self):
        self.add_part(self.body[-1].position())

    def move(self):
        for part_num in range (len(self.body) - 1, 0, -1):
            x = self.body[part_num - 1].xcor()
            y = self.body[part_num - 1].ycor()
            self.body[part_num].goto(x,y)
        self.head.fd(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)