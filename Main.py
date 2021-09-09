from turtle import *


screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor("red")
screen.colormode(255)

kingTurt = Turtle()
kingTurt.shape("turtle")
kingTurt.resizemode("auto")
kingTurt.width(3)
kingTurt.pencolor("blue")
kingTurt.speed(0)
#screen.tracer(0)

def line(length, direction):
    #kingTurt.setheading(direction)
    kingTurt.left(direction)
    kingTurt.forward(length)
    return
    



def recurse(tik, baseSize, red, green, blue, xpos, ypos):
    
    print(tik)

    kingTurt.pencolor(red, green, blue)
    line(baseSize, 20)
    
    if tik <= 0:
        return
    else:
        tik -= 1
        recurse(tik, baseSize*.5, red, green+10, blue, xpos, ypos)
        recurse(tik, baseSize*.5, red, green+10, blue, xpos, ypos)

kingTurt.penup()
kingTurt.setposition(0, -400)
kingTurt.pendown()

kingTurt.setheading(90)

recurse(3, 100, 0, 0, 0, 0, -400)


#screen.update()


h=input("") 
