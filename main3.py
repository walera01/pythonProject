import turtle
import random
import math
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.pencolor('red')
a=0
d=0
r=80
g=200
b=70
f=5
t.speed(0)
t.penup()
t.goto(0,200)
t.pendown()
turtle.colormode(255)
while(True):
    t.forward(a)
    t.right(d)
    a-=4
    d-=1
    if r==200:
        f=-10
    elif r==80:
        f = 5
    r+=f
    g=int(abs(math.sin(r))*200)
    b=int(abs(math.cos(r))*200)
    t.pencolor(r,g,b)
    if d==210:
        break
    t.hideturtle()
turtle.done()