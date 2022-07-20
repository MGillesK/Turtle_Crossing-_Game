from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.color("black")
        self.level = 1
        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_score()

    def end_of_game(self):
        self.goto(0,0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)