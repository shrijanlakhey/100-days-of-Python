from turtle import Turtle, Screen
from random import choice
timmy = Turtle()
color_choices = ['blue', 'dark red', 'green', 'burlywood', 'indigo', 'dark orange', 'light slate gray', 'navy']

def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range(num_sides):
        timmy.right(angle)
        timmy.forward(100)

for n_sides in range(3, 11):
    timmy.color(choice(color_choices))
    draw_shape(n_sides)


screen = Screen()
screen.exitonclick()