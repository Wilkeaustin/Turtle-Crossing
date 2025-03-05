from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")

        self.hideturtle()
        self.level = 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=FONT)

    def game_level(self):
        self.penup()
        self.goto(-280, 260)
        self.color("black")
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

    def level_up(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="left", font=FONT)

