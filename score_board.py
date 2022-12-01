from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')
BIG_FONT = ('Courier', 30, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-20, 270)
        self.color("white")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        print(f"The Score is {self.score}")

    def calculate_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=BIG_FONT)
