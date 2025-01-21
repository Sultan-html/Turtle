import turtle

def draw_heart():
    turtle.penup()
    turtle.goto(0, -200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("red")
    turtle.left(50)
    turtle.forward(133)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.left(120)
    for _ in range(200):
        turtle.right(1)
        turtle.forward(2)
    turtle.forward(133)
    turtle.end_fill()