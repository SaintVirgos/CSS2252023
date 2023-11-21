#Zaineb Bonilla
#11/20/2023
#Problem 5: Use the following chunk of code as a base to produce the image shown below.

import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a sqaure of sz side"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

for i in range(1,6):
    drawSquare(alex, i*20)
    alex.left(225)
    alex.up()
    alex.forward(15)
    alex.down()
    alex.right(225)

wn.exitonclick()