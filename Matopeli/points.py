from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Points(Turtle):
    def __init__(self):
        super().__init__()
        self.scored = 0
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update_scored()
        self.hideturtle()

    def update_scored(self):
        self.write(f"Points = {self.scored}\nESC to Quit", align=ALIGNMENT, font=FONT)

    def set_score(self):
        self.clear()
        self.scored += 1
        self.update_scored()

    def game_over_text(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
