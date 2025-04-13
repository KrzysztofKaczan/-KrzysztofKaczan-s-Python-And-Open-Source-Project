from turtle import Screen, Turtle
import time
from snake import Snake 
from food import Food
from scoreborde import Scorebord
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Gra PL Super Chomikuj.pl")
screen.tracer(0)

scorebord = Scorebord()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

def restart_game():
    global game_on
    game_on = True
    scorebord.reset_score()  
    snake.reset_position()    
    food.refresh()          
    game_loop()             

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #colision 
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebord.increase_score()

    #wall col 
    if snake.head.xcor()>290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        scorebord.game_over()

    #ogonwazki 
    for segment in snake.segments[1:]:
         if snake.head.distance(segment) < 10: 
            game_on = False 
            scorebord.game_over()

screen.onkey(restart_game, "r")  

game_loop()
    
screen.exitonclick()
