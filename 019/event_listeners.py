from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(50)

screen.listen()
# when we use a function as an argument, we don't add parentheses '()' to the end of it as adding '()' will trigger the function
screen.onkey(key="space", fun=move_forward) 
screen.exitonclick()
