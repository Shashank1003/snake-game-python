from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.write(
            f"Score: {self.score}",
            False,
            align="center",
            font=("Verdana", 10, "normal"),
        )

    def add_score(self):
        self.score = self.score + 1
        self.clear()
        self.write(
            f"Score: {self.score}",
            False,
            align="center",
            font=("Verdana", 10, "normal"),
        )

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER!",
            False,
            align="center",
            font=("Verdana", 28, "normal"),
        )
