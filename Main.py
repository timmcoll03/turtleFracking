from turtle import *
import random
import math
kick=10


screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("#afdeee")
screen.colormode(255)

kingTurt = Turtle()
kingTurt.shape("turtle")
kingTurt.resizemode("auto")
kingTurt.width(3)
kingTurt.pencolor("blue")
kingTurt.speed(0)
screen.tracer(0)

        
def stupid_line(length,angle):
    kingTurt.forward(length)
    return

def goto(x,y):
    kingTurt.penup()
    kingTurt.goto(x,y)
    kingTurt.pendown()


kingTurt.seth(90)
def tree(kick,length,angle):    
    if kick>=0:
        
        kick-=1
        stupid_line(length,angle)
        new_length=length-5
        kingTurt.left(angle)
        tree(kick, new_length,angle)
        kingTurt.right(angle*2)
        tree(kick, new_length,angle)
        kingTurt.left(angle)
        kingTurt.backward(length)
        return
    
def snowflake(size,spindle, angle):
    for quant in range(spindle):
        kingTurt.seth((360/spindle)*quant)
        tree(5,size,angle)
        

   

for snow in range (8):
    for snowy in range (30):
        goto(-500+(snowy*33),400-(snow*100)+random.randint(0,70))
        if random.randint(5-snow,7) == 7:
            snowflake(random.randint(16,20),random.randint(6,8),30)

goto(-500,-450)
kingTurt.seth(270)

x=-500
y=-450
for line in range(1000):
    kingTurt.setposition(x,y)
    x = x+1
    y = (3*math.sin(.04*x))-400
    kingTurt.pendown()

kingTurt.seth(90)
goto(0,-400)

#tree(15, 80, 20)

screen.update()
hideturtle()


h=input("") 
