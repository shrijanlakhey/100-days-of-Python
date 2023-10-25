import turtle as t
from random import choice, randint

directions = [ 0, 90, 180, 270]

timmy = t.Turtle()
t.colormode(255)

timmy.pensize(15)
timmy.speed("fastest")

# tuple eg, my_tuple = (1,2,3), it has round bracket around it 
# we can't change values in tuples like how we can do it with lists
# but we can make changes to it byt convertig it into a list
# eg, list(my_tuple), which converts the tuple into a list

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b) # tuple
    return random_color

for i in range(200):
    timmy.setheading(choice(directions))
    timmy.forward(25)
    timmy.color(random_color())

screen = t.Screen()
screen.exitonclick()

