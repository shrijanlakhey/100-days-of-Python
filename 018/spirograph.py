import turtle as t
from random import choice, randint

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirogaph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)

        # -----------------------------------------------
        timmy.left(size_of_gap)
        # alternative way:
        # timmy.setheading(timmy.heading() + size_of_gap)
        # -----------------------------------------------

draw_spirogaph(5)
screen = t.Screen()
screen.exitonclick()