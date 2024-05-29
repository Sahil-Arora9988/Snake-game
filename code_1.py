from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")

snake = Snake()

screen.update()
while True:
    time.sleep(0.20)
    snake.move_snake()
    snake.up()
    screen.update()
















screen.exitonclick()