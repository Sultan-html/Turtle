import turtle

turtle.setup(300, 300)
window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(1)

def draw_heart():
    pen.penup()
    pen.goto(0, -70)
    pen.pendown()
    pen.color("red")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

draw_heart()

pen.penup()
pen.goto(-54, 0)
pen.color("white")
pen.write("Раяна", font=("Courier", 24, "bold"))

pen.hideturtle()

turtle.done()
#i love