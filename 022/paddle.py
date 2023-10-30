from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        y_cor = self.ycor() + MOVE_DISTANCE 
        self.goto(x=self.xcor(), y=y_cor)

    def down(self):
        # self.paddles[0].setheading(DOWN)
        y_cor = self.ycor() - MOVE_DISTANCE 
        self.goto(x=self.xcor(), y=y_cor)