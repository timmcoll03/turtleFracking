from turtle import *
import random
kick=5

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
        


for snow in range (5):
    for snowy in range (6):
        goto(random.randint(-500, 500),random.randint(150,300))


        snowflake(random.randint(15,18),random.randint(2,5),30)





screen.update()


h=input("") 
