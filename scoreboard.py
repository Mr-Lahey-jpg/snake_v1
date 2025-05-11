from turtle import Turtle,Screen

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.write(arg="Score: ",align="center")

scoreboard = Scoreboard()

screen = Screen()
screen.exitonclick()
