"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
from math import ceil
t = turtle.Turtle()

def square(sidelength):
  for i in range(4):
    t.fd(sidelength)
    t.lt(90)
square(75)

t.reset()

def triangle(sidelength):
  for i in range(3):
    t.fd(sidelength)
    t.lt(120)
triangle(75)
t.reset()
def pentagon(sidelength):
  for i in range(5):
    t.fd(sidelength)
    t.lt(72)
pentagon(75)
t.reset()
def dodecagon(sidelength):
  for i in range(12):
    t.fd(sidelength)
    t.lt(30)
dodecagon(30)
t.reset()
t.speed(412979812749827)
def circle(length):
  for i in range(int(ceil(360/length))):
    t.fd(length)
    t.lt(length)
circle(1)
t.hideturtle()