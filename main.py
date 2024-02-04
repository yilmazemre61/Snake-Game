from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # It sets the animation OFF

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()  # To listen the keyboard actions
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


"""Creating the Snake move forward automatically"""
game_is_on = True
while game_is_on:
    """It will update all the segments once they all move to new position"""
    screen.update()
    time.sleep(0.1)

    snake.move()
    """Detect collusion with food"""
    if snake.head.distance(food) < 15:
        food.refresh_food_location()
        snake.extend()
        scoreboard.update_score()

    """Detect collusion with the wall"""
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 370 or snake.head.ycor() < -390:
        scoreboard.reset()
        snake.reset()

    """Detect collision with tail"""
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
