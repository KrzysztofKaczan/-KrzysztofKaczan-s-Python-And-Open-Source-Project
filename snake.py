STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
from turtle import Turtle
class Snake: 
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
         segment_new = Turtle("square")
         segment_new.color("white")
         segment_new.penup()
         segment_new.goto(position)
         self.segments.append(segment_new)

    def move(self):
          for seg_num in range(len(self.segments) -1, 0, -1):
             new_x =  self.segments[seg_num - 1].xcor()
             new_y =  self.segments[seg_num - 1].ycor()
             self.segments[seg_num].goto(new_x,new_y)
          self.segments[0].forward(MOVE_DISTANCE)   
   