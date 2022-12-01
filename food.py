import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.penup()
        self.refresh_location()

    def refresh_location(self):
        xcor = random.randint(-270, 270)
        ycor = random.randint(-270, 270)
        self.goto(xcor, ycor)



