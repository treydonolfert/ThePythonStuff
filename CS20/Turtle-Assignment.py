#Treydon Olfert
#January 17th, 2023
#Turtle Assignment
#Computer Science 20
#---------------------------------------------------
import turtle
from time import sleep
t = turtle.Turtle()
    
def triangle(sidelength):
  for i in range(3):
    t.fd(sidelength)
    t.lt(120)

def rectangle():
  for i in range(2):
    t.fd(75)
    t.lt(90)
    t.fd(30)
    t.lt(90)

def square():
  for i in range(4):
    t.fd(75)
    t.lt(90)

def trianglefractal(layers, size): #This is used for part 2 of the assignment. When calling the function, it will create a Sierpinski Triangle and takes two parameters: layers and size. Layers determines how deep the fractal goes and size is the side length of the entire shape. It works by stacking the function for as many layers as needed and when it reaches the bottom (layers = 0) it draws and fills a yellow triangle. It draws the shape by drawing all the smallest triangles and for every 2 triangles, it goes to the top of them and draws another one.
  if layers == 0:
    t.begin_fill()
    triangle(size)
    t.end_fill()
  else:
    trianglefractal(layers-1, size/2) #Stacks functions and the size gets halved each time so the smallest triangles that need to be drawn are the appropriate size
    t.fd(size/2) #When the last stacked function ends, it goes here. Going forward size/2 will mean the turtle will go to the bottom right corner of the triangle (or the last layer of the Sierpinski Triangle it just drew) and is ready to draw the next one.
    trianglefractal(layers-1, size/2)
    #After drawing a second triangle, it will go backwards, left, forward, and right to arrive at the top of the first triangle where it can draw the next triangle
    t.back(size/2)
    t.lt(60)
    t.fd(size/2)
    t.rt(60)
    trianglefractal(layers-1, size/2)
    #After drawing a third triangle, it heads back to the bottom left of the shape to prepare for the next stack.
    t.lt(60)
    t.back(size/2)
    t.rt(60)
#---------------------------------------------------
#Rectangle cross
for i in range(4):
  rectangle()
  t.lt(90)

sleep(3)
t.reset()
#---------------------------------------------------
#Triangle hexagon
for i in range(6):
  triangle(75)
  t.rt(60)

sleep(3)
t.reset()
#---------------------------------------------------
#Square and rotated square
square()
t.up()
t.fd(37.5)
t.rt(90)
t.fd(15)
t.lt(135)
t.pd()
square()

sleep(3)
t.reset()
#---------------------------------------------------
#Sierpinski Triangle
turtle.Screen().bgcolor("black")
t.speed(0)
t.hideturtle()
t.pu()
t.setpos(-200, -150)
t.color("yellow")
t.pd()
trianglefractal(6, 500) #I tested other values for these and determined that 6 and 500 were the coolest looking.