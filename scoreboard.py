FONT = ("Courier", 24, "bold")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)
