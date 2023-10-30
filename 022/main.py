from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# creating paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# creating ball
ball = Ball()
game_is_on = True

scoreboard = ScoreBoard()
screen.listen()

# movement keys for left paddle
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

# movement keys for right paddle
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    ball.move()


    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print("made contact")
        ball.bounce_x()

    # Detect if r_paddle missed
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect if l_paddle missed
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()