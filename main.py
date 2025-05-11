from turtle import Screen
from game.snake import Snake
from game.food import Food
from game.scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("SNAKE")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_points()

screen.exitonclick()