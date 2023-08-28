from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 20, 'normal')
LOCATION = (0, 250)

with open("data.txt", mode="r") as data_score:
    SCORE = int(data_score.read())


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score_num = 0
        self.penup()
        self.high_score = SCORE
        self.hideturtle()
        self.goto(LOCATION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Score = {self.score_num} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def score_count(self):
        self.score_num += 1
        self.update_score()

    def reset(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", mode="w") as data_input:
                data_input.write(str(self.high_score))
        self.score_num = 0
        self.update_score()
