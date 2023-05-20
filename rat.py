from turtle import Turtle
from random import randint


class Rat(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.reposition()

    def reposition(self):
        randX = randint(-280, 280)
        randY = randint(-280, 280)
        self.goto(randX, randY)
