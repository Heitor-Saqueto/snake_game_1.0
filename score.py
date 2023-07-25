from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 20, 'normal')
LOCATION = (0, 250)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_num = 0
        self.goto(LOCATION)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Score = {self.score_num}", align=ALIGN, font=FONT)

    def score_count(self):
        self.score_num += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER ", align=ALIGN, font=FONT)





