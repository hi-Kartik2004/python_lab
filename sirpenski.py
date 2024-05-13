from turtle import *
screen = Screen()

def sirpenski(side, n):
    if n == 0:
        return
    for _ in range(3):
        forward(side)
        left(120)
        sirpenski(side/2, n-1)

sirpenski(100, 3)


screen.exitonclick()