import turtle
import random
import matplotlib.pyplot as plt
import math

# To visualize the random points:
myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)

# Drawing a square:
myPen.up()
myPen.setposition(-100, -100)
myPen.down()
myPen.fd(200)
myPen.left(90)
myPen.fd(200)

myPen.left(90)
myPen.fd(200)
myPen.left(90)
myPen.fd(200)
myPen.left(90)

# Drawing a circle:
myPen.up()
myPen.setposition(0, -100)
myPen.down()
myPen.circle(100)
