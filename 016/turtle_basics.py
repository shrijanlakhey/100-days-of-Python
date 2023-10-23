# note in oop, we give name to the class in Pascal case. eg, CarBlueprint()
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("Blue","CadetBlue")
timmy.forward(100)

my_screen = Screen()

print(my_screen.canvheight) # accessing the attributes of the Screen() class
my_screen.exitonclick() # accessing a method of the Screen() class