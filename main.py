from turtle import Screen
import time
from snake import Snake
from rat import Rat
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
is_game_on = True


snake = Snake()
rat = Rat()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.up, "Up")

screen.onkey(snake.down, "s")
screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "a")
screen.onkey(snake.left, "Left")

screen.onkey(snake.right, "d")
screen.onkey(snake.right, "Right")

screen.onkey(screen.bye, "q")
screen.onkey(screen.bye, "Escape")


screen.update()

while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake.moveFwd()

    if snake.segments[0].distance(rat) < 10:
        rat.reposition()
        scoreboard.add_score()
        snake.grow()

    if (
        snake.segments[0].xcor() > 285
        or snake.segments[0].xcor() < -285
        or snake.segments[0].ycor() > 285
        or snake.segments[0].ycor() < -285
    ):
        is_game_on = False
        scoreboard.game_over()

    for square in snake.segments[1:]:
        if square.distance(snake.segments[0]) == 0:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
