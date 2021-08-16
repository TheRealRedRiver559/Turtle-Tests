import turtle
import random
import time

wn = turtle.Screen()
wn.title('Turtle Chase Test')
wn.bgcolor('black')
wn.screensize(320,320)
wn.setup(width=320, height=320,startx=None,starty=None)
wn.tracer(0)

border = turtle.Turtle()
border.penup()
border.pencolor('white')
border.pensize(3)
border.goto(-317, -317)
border.pendown()
border.hideturtle()
for x in range(4):
    border.forward(617)
    border.left(90)

player = turtle.Turtle()
player.color('white')
player.penup()

line = turtle.Turtle()
line.color('#' + ''.join(random.sample('0123456789ABCDEF', 6)))
line.speed(1)
line.hideturtle()

turtles = []
for x in range(20):
    x = turtle.Turtle()
    x.color('#' + ''.join(random.sample('0123456789ABCDEF', 6)))
    x.speed(2)
    x.penup()
    x.shape('turtle')
    x.setheading(random.randint(1, 360))
    x.setpos(random.randint(-300, 300), random.randint(-300, 300))
    turtles.append(x)

def left():
    player.setheading(player.heading() + 5)
def right():
    player.setheading(player.heading() - 5)

def collisions():
    if player.xcor() >= 299 or player.xcor() <= -299:
        player.setheading(180-player.heading())
    if player.ycor() >= 299 or player.ycor() <= -299:
        player.setheading(player.heading() *-1)

    for turtle in turtles:
        if turtle.xcor() >= 299 or turtle.xcor() <= -299:
            turtle.setheading(180-turtle.heading())
        if turtle.ycor() >= 299 or turtle.ycor() <= -299:
            turtle.setheading(turtle.heading() *-1)

def main():
    while True:
        wn.listen()
        time.sleep(0.001)
        collisions()
        player.forward(1.5)
        line.clear()
        for turtle in turtles:
            turtle.forward(0.5)
        for i in range(len(turtles)):
            for _ in range(i, len(turtles)+1):
                if turtles[i].distance(player) < 200:
                    heading = turtles[i].towards(player.pos())
                    turtles[i].setheading(heading)
                
        for turtle in turtles:
            length = turtle.distance(player.pos())
            if length < 200:
                line.penup()
                line.goto(turtle.pos())
                line.pendown()
                line.goto(player.pos())
        wn.onkeypress(left, 'a')
        wn.onkeypress(right, 'd')


        wn.update()
main()
