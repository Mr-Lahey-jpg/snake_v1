from turtle import Turtle,Screen
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=260)
        self.pencolor("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align= ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()






