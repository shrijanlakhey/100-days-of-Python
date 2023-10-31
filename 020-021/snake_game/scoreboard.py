from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("020-021/snake_game/data.txt") as data:
            self.highscore=int(data.read())
        self.penup()
        self.color("white")
        self.setposition(x=0,y=260)
        self.hideturtle()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    # def game_over(self):
    #     self.setposition(0,0)
    #     self.write(arg="GAME OVER.", move=False, align=ALIGNMENT, font=FONT)
    

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("020-021/snake_game/data.txt", mode="w") as data:
                data.write(f"{self.highscore}") # writing a string to the file
                
        self.score = 0
        self.update_scoreboard()
        
            


        
            