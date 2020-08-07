#Very Simple Snake Game Using Python3(Turtle) By-Arun Mathai

import turtle
import time
import random

delay = 0.1
score = 0
highscore = 0

window = turtle.Screen()
window.title("Snake Game By - Arun Mathai")
window.bgcolor("black")
window.setup(width =600,height = 600)
window.tracer(0)

snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("yellow")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction = "stop"

snake_food= turtle.Turtle()
snake_food.speed(0)
snake_food.shape("circle")
snake_food.color("red")
snake_food.penup()
snake_food.goto(0,100)


snake_body_parts = []

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.shape("circle")
score_pen.color("blue")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0,260)
score_pen.write("Score:"+str(score)+"   "+" High Score:"+str(highscore),align = "center",font =("Courier",24,"normal"))





def snake_head_movement():
    if snake_head.direction == "up":
        snake_head.sety(snake_head.ycor()+10)

    if snake_head.direction == "down":
        snake_head.sety(snake_head.ycor()-10)

    if snake_head.direction == "left":
        snake_head.setx(snake_head.xcor()-10)

    if snake_head.direction == "right":
        snake_head.setx (snake_head.xcor()+10)

def snake_head_goup():
    if(snake_head.direction != "down"):
        snake_head.direction = "up"
    
def snake_head_godown():
     if(snake_head.direction != "up"):
         snake_head.direction = "down"
    
def snake_head_goleft():
     if(snake_head.direction != "right"):
         snake_head.direction = "left"
    
def snake_head_goright():
     if(snake_head.direction != "left"):
         snake_head.direction = "right"

def gameover():
    global delay
    global score
    global highscore
    delay=0.1
    for parts in snake_body_parts:
            parts.goto(5000,5000)
    snake_body_parts.clear()
    if(score >= highscore):
        highscore=score        
    score=0
    score_pen.clear()
    score_pen.write("Score:"+str(score)+"   "+" High Score:"+str(highscore),align = "center",font =("Courier",24,"normal"))
    time.sleep(0.4)
    snake_head.goto(0,0)
    snake_head.direction ="stop"

window.listen()
window.onkeypress(snake_head_goup,"Up")
window.onkeypress(snake_head_godown,"Down")
window.onkeypress(snake_head_goleft,"Left")
window.onkeypress(snake_head_goright,"Right")


            
while True:
    window.update()
    
    if(snake_head.xcor()>290 or snake_head.xcor()<-290 or snake_head.ycor()>290 or snake_head.ycor()<-290):
        gameover()

            
    if(snake_head.distance(snake_food)<10):
        score+=1
        score_pen.clear()
        score_pen.write("Score:"+str(score)+"   "+" High Score:"+str(highscore),align = "center",font =("Courier",24,"normal"))
        snake_food.goto(random.randint(-290,290),random.randint(-290,290))
        new_snake_body_part = turtle.Turtle()
        new_snake_body_part.speed(0)
        new_snake_body_part.shape("square")
        new_snake_body_part.color("green")
        new_snake_body_part.penup()
        snake_body_parts.append(new_snake_body_part)
        if((delay-(score*0.0005))>0.):
           print(delay)
           delay=delay-(score*0.0005)
           
           
    for parts in range(len(snake_body_parts)-1,0,-1):         
        snake_body_parts[parts].goto(snake_body_parts[parts-1].xcor(),snake_body_parts[parts-1].ycor())
    if(len(snake_body_parts)>0):
        snake_body_parts[0].goto(snake_head.xcor(),snake_head.ycor()) 
        
       
    snake_head_movement()

    for parts in snake_body_parts:
        if(parts.distance(snake_head)<10):
            gameover()
        

    
    time.sleep(delay)
     
 


window.mainloop()
