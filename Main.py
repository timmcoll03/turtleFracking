# "Snowy Wonderland" Written by Timothy Colledge, Hunter Allen, and Kevin Cavicchia
# CITE: Timothy Colledge
# CITE: Hunter Allen
# CITE: Kevin Cavicchia
# Libraries Used:
#   turtle - https://docs.python.org/3/library/turtle.html
#   math - https://docs.python.org/3/library/math.html
#   random - https://docs.python.org/3/library/random.html
# Software Used
#   Thonny 
#   Visual Studio Code
#   GitHub


# Imports
from turtle import *
import random
import math


#Enviroment Initialization
screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("#afdeee")
screen.colormode(255)

#Creating Turtle and Settings its Attributes
kingTurt = Turtle()
kingTurt.shape("turtle")
kingTurt.resizemode("auto")
kingTurt.width(3)
kingTurt.pencolor("blue")
kingTurt.speed(0)
screen.tracer(0)
kingTurt.seth(90)


# Simple Function that Takes in lenght and goes forward that length and sends the turtle forward that direction
# This Function does not do anything unique compared to forward but exists for further expandibility    
def stupid_line(length):
    kingTurt.forward(length)
    return

# This allows us to send the turtle somewhere based on x,y cordinates 
# However, this also has built in pen features as compared to the turtle library goto() function
def goto(x,y):
    kingTurt.penup()
    kingTurt.goto(x,y)
    kingTurt.pendown()

# tree fun uses recursion to draw a tree given imputs for the recusion count [kick] and length and angle of the tree branches
def tree(kick,length,angle):    
    if kick>=0:       
        kick-=1
        stupid_line(length)
        new_length=length-5
        kingTurt.left(angle)
        tree(kick, new_length,angle)
        kingTurt.right(angle*2)
        tree(kick, new_length,angle)
        kingTurt.left(angle)
        kingTurt.backward(length)
        return

# This uses the tree function but in effect "spins" it, the imputs are the same as tree except the recursion 
# size is always five the only thing we change is the size
# and spindle count [which refrers to the number of "trees" used in one flake]    
def snowflake(size,spindle, angle):
    for quant in range(spindle):
        kingTurt.seth((360/spindle)*quant)
        tree(5,size,angle)
        
# Tree Creation 
kingTurt.pensize(1)
kingTurt.pencolor("brown")
kingTurt.seth(90)
goto(-300,-400)
tree(6, 80, 20)
goto(-175,-400)
tree(5, 80, 20)
goto(100,-400)
tree(4, 80, 20)   

# Snow Creation
kingTurt.pencolor("white")

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

#Cloud Creation
kingTurt.pencolor("grey")
for cloud in range(12):
    goto(-600+(100*cloud),550)
    kingTurt.pensize(100)
    kingTurt.circle(100,360)
    kingTurt.pensize(1)

#draws each brick
kingTurt.setheading(180)

def brick(xLoc, yLoc):
    kingTurt.color("maroon")
    kingTurt.pencolor("white")    
    kingTurt.up()
    kingTurt.goto(xLoc, yLoc)
    kingTurt.down()
    kingTurt.begin_fill()
    for rectangle in range(2):
        kingTurt.forward(30)
        kingTurt.right(90)
        kingTurt.forward(15)
        kingTurt.right(90)
    kingTurt.end_fill()

#draws rows of bricks
xLoc = 430
for number in range(5):
    brick(xLoc, -400)
    xLoc = xLoc - 30

xLoc = 430
for number in range(5):
    brick(xLoc, -385)
    xLoc = xLoc - 30

xLoc = 430
for number in range(5):
    brick(xLoc, -370)
    xLoc = xLoc - 30

xLoc = 430
for number in range(5):
    brick(xLoc, -355)
    xLoc = xLoc - 30

xLoc = 430
for number in range(5):
    brick(xLoc, -340)
    xLoc = xLoc - 30

xLoc = 430
for number in range(5):
    brick(xLoc, -325)
    xLoc = xLoc - 30

xLoc = 430
for number in range(5):
    brick(xLoc, -310)
    xLoc = xLoc - 30
   
#draws chimney
kingTurt.penup()
kingTurt.color("sienna")
kingTurt.pencolor("saddle brown")
kingTurt.goto(400,-280)
kingTurt.pendown()
kingTurt.begin_fill()
kingTurt.setheading(90)
for chimney in range(2):
    kingTurt.forward(75)
    kingTurt.right(90)
    kingTurt.forward(30)
    kingTurt.right(90)
kingTurt.end_fill()

#draws roof
kingTurt.penup()
kingTurt.color("saddle brown")
kingTurt.pencolor("sienna")
kingTurt.goto(450,-295)
kingTurt.pendown()
kingTurt.begin_fill()
kingTurt.setheading(135)
kingTurt.forward(math.sqrt(18050))
kingTurt.left(90)
kingTurt.forward(math.sqrt(18050))
kingTurt.setheading(0)
kingTurt.forward(190)
kingTurt.end_fill()

#draws door
kingTurt.penup()
kingTurt.color("sienna")
kingTurt.pencolor("saddle brown")
kingTurt.goto(340, -400)
kingTurt.pendown()
kingTurt.begin_fill()
for door in range(2):
        kingTurt.forward(30)
        kingTurt.left(90)
        kingTurt.forward(50)
        kingTurt.left(90)
kingTurt.end_fill()

#draws door handle
kingTurt.penup()
kingTurt.color("gold")
kingTurt.pencolor("goldenrod")
kingTurt.goto(362, -380)
kingTurt.pendown()
kingTurt.begin_fill()
kingTurt.circle(2.5)
kingTurt.end_fill()


#Cleanup Code and KillSwitch for running in IDEs other than Thonny
screen.update()
hideturtle()
h=input("") 