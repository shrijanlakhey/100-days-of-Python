from turtle import Turtle

ALIGNMENT = "center"

class State(Turtle):
    def __init__(self,state_name, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.setposition(x=x_cor,y=y_cor)
        self.hideturtle()
        self.write(state_name)