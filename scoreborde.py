from turtle import Turtle


class Scorebord(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0 
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.hideturtle()
        self.update_score()
        
    def update_score(self): 
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 24, "normal"))

    def game_over(self): 
         self.goto(0,0)
         self.write(f"GAME OVER\n press r to reset", align = "center", font = ("Arial", 24, "normal"))
    
    def increase_score(self): 
        self.score += 1 
        self.clear()
        self.update_score()

    def reset_score(self):
        self.clear()
        self.goto(0, 250)
        self.score = 0
        self.update_score()
        