from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) # turns animations off


snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.listen()
game_is_on = True

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
while game_is_on:
    screen.update() # turns animation on
    time.sleep(0.1)
    
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) < 15: # checks if the distance between the head of the snake and the food is less than 15
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 265 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision wth tail
    for segment in snake.segments[1:]: # looping through all the items in segment excep the first one
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()