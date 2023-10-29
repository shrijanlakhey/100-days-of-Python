from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.setposition(x=0,y=260)
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        
    
    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.setposition(0,0)
        self.write(arg="GAME OVER.", move=False, align=ALIGNMENT, font=FONT)
