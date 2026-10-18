import turtle

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

# Draw polygon
sides = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))

angle = 360 / sides

for i in range(sides):
    t.forward(length)
    t.right(angle)

# Koch curve
def koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        length = length / 3

        koch(length, depth - 1)
        t.left(60)
        koch(length, depth - 1)
        t.right(120)
        koch(length, depth - 1)
        t.left(60)
        koch(length, depth - 1)

# Move turtle to another position
t.penup()
t.goto(-150, -100)
t.pendown()

depth = int(input("Enter Koch fractal depth: "))

for i in range(3):
    koch(300, depth)
    t.right(120)

turtle.done()