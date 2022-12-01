import time

from snake import Snake
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snak = Snake()
screen.tracer(0)

while True:
    screen.update()
    time.sleep(1)
    snak.move()
screen.exitonclick()