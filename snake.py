from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]

    def create_snake(self):
        for position in START_POSITIONS:
            obj = Turtle("square")
            obj.color("white")
            obj.penup()
            obj.goto(position)
            self.turtle_list.append(obj)

    def grow_snake(self):
        obj = Turtle("square")
        obj.color("white")
        obj.penup()
        self.turtle_list.append(obj)

    def move(self):
        for ele in range(len(self.turtle_list) - 1, 0, -1):
            xcor = self.turtle_list[ele - 1].xcor()
            ycor = self.turtle_list[ele - 1].ycor()
            self.turtle_list[ele].goto(xcor, ycor)
        self.turtle_list[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)