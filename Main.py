from turtle import *


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
#screen.tracer(0)





        
def stupid_line(length,angle,x,y):
    kingTurt.forward(length)
    return



kick=5
kingTurt.seth(90)
def tree(kick,length,angle,xpos,ypos):
    if kick>=0:
        stupid_line(length,angle,xpos,ypos)
        new_length=length-5
        kingTurt.left(angle)
        tree(kick, new_length,angle,xpos,ypos)
        kingTurt.right(angle*2)
        tree(kick, new_length,angle,xpos,ypos)
        kingTurt.left(angle)
        kingTurt.backward(length)
        kick-=1

        return
tree(kick,100,30,25,60)
    








#screen.update()


h=input("") 
