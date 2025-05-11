from turtle import Turtle,Screen



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0,y=260)
        self.pencolor("white")
        self.write(arg=f"Score: 0",align="center",font=('arial',20,'normal'))

    def add_points(self):
        self.current_score += 1
        self.clear()
        self.write(arg=f"Score: {self.current_score}", align="center", font=('arial', 20, 'normal'))




