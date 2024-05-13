import turtle


def koch_fractal(length, n):
    if n == 0:
        turtle.forward(length)
        return
    else:
        koch_fractal(length, n-1)
        turtle.left(60)
        koch_fractal(length, n-1)
        turtle.left(-120)
        koch_fractal(length, n-1)
        turtle.left(60)
        koch_fractal(length, n-1);

turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
koch_fractal(30, 2)
turtle.done()
