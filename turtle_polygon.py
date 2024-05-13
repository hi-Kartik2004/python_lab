import turtle

def displayPolygon(n , length):
    angle = 360/n
    turtle.pencolor('red')
    for i in range(n):
        turtle.forward(length)
        turtle.left(angle)
    
    turtle.done()


n = int(input("Enter the sides: "))
length = int(input("Enter the length: "))

displayPolygon(n, length)
