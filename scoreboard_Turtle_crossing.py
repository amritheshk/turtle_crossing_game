from turtle import Turtle
FONT = ("Courier", 24, "normal")
FONT_L=("Courier",15,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level=1
    def update_score(self):
        self.clear()
        self.goto(-280,250)
        self.write(arg=f"Level:{self.current_level}",align="left",font=FONT_L)
    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write("GAME OVER",align="center",font=FONT)
    def level_up(self):
        self.current_level+=1
