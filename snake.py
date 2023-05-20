import turtle as t
import time


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.segments[0].shape("arrow")

    def create_snake(self):
        for i in range(0, 3):
            square = t.Turtle(shape="square")
            square.color("yellow")
            square.penup()
            square.goto(-10 * i, 0)
            square.shapesize(stretch_wid=0.5, stretch_len=0.5)
            self.segments.append(square)

    def moveFwd(self):
        for square_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square_index - 1].xcor()
            new_y = self.segments[square_index - 1].ycor()
            self.segments[square_index].goto(new_x, new_y)

        self.segments[0].forward(10)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def grow(self):
        new_square = t.Turtle(shape="square")
        new_square.color("yellow")
        new_square.penup()
        new_square.goto(self.segments[-1].position())
        new_square.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.segments.append(new_square)
