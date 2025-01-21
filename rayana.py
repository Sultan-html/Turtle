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

def write_name():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.color("white")
    turtle.hideturtle()
    turtle.write("Раяна", align="center", font=("Arial", 24, "bold"))

def main():
    turtle.speed(5)
    draw_heart()