import turtle
from turtle import *
from turtle import Screen
<<<<<<< HEAD
    
=======

>>>>>>> 63b362bf37233e249d78dd2afc1530b1ec5c390f
def emptySquare():
    
    t = turtle.Turtle()
    for i in range(4):
        t.forward(50)
        t.right(90)     # Rotate clockwise by 90 degrees
    
<<<<<<< HEAD
def filledSquare():
    s = int(input("Enter the length of the side of the square: ")) 
    col = input("Enter the color name or hex value of color(# RRGGBB): ") 
    t = turtle.Turtle()
    t.fillcolor(col)
    t.begin_fill()
    for i in range(4):
        t.forward(s)
        t.right(90)     # Rotate clockwise by 90 degrees
    t.end_fill()

    pass  # TODO
 
=======
def emptyCircle():
    t = turtle.Turtle()
    t.circle(100)

def filledCircle():
    t = turtle.Turtle()
    t.fillcolor('red')  # set the fillcolor
    t.begin_fill()  # start the filling color 
    t.circle(100)
    t.end_fill()

>>>>>>> 63b362bf37233e249d78dd2afc1530b1ec5c390f
  
while True:
    screen = Screen()
    answer = screen.textinput("Next Game","1 - Square:")
    if (answer is None):
        break
    elif (answer == '1'):
        emptySquare()
    elif (answer == '2'):
        filledSquare()
    elif (answer == '3'):
        emptyCircle()
    elif (answer == '4'):
        filledCircle() 
