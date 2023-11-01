from turtle import Turtle, Screen
from Movement import Movement
import time

screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

move = Movement()

snake = []
position = ((0, 0), (-20, 0), (-40, 0))

for item in range(3):
    segment = Turtle()
    segment.penup()
    segment.shape("square")
    segment.color("white")
    snake.append(segment)
    segment.goto(position[item])

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(snake) - 1, 0, -1):
        new_x = snake[segment - 1].xcor()
        new_y = snake[segment - 1].ycor()
        snake[segment].goto(new_x, new_y)
    # snake[0].fd(10)
    screen.listen()
    screen.onkey(move.move_right, "w")




screen.exitonclick()