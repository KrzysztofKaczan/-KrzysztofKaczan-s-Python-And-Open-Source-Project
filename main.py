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

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #colision 
    if snake.head.distance(food) < 15:
        food.refresh()
        scorebord.increase_score()

    
screen.exitonclick()