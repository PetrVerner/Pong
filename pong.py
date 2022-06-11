import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("#008000")
wn.setup(width=800, height=600, startx=True, starty=True)
wn.tracer(0, 1)

# Federer
federer = turtle.Turtle()
federer.speed(0)
federer.shape("turtle")
federer.color("#FF0000")
federer.shapesize(stretch_wid=3, stretch_len=3, outline=6)
federer.penup()
federer.goto(-350, 0)

# Nadal
nadal = turtle.Turtle()
nadal.speed(0)
nadal.shape("square")
nadal.color("#FF8000")
nadal.shapesize(stretch_wid=8, stretch_len=1, outline=6)
nadal.penup()
nadal.goto(350, 0)
nadal.dy = 0.6

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("#FFFF00")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Roger Federe: 0 Rafael Nadal: 0", align="center", font=("Courier", 24, "normal"))

# function
def federer_up():
    y = federer.ycor()
    y += 20
    federer.sety(y)
    federer.setheading(y)


def federer_down():
    y = federer.ycor()
    y -= 20
    federer.sety(y)
    federer.setheading(y)

# keyboard binding
wn.listen()
wn.onkeypress(federer_up, "Up")
wn.onkeypress(federer_down, "Down")

# main game loop
while True:
    wn.update()
    wn.listen(30, 40)