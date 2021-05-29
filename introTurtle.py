import turtle
import random

turtle.bgcolor("black")
turtle.screensize(800, 400) # de -400 a 400 en x y de -200 a 200 en y

bob = turtle.Turtle()
bob.color("red")
bob.penup()
bob.goto(-400, 0)
bob.pendown()

steve = turtle.Turtle()
steve.color("blue")
steve.penup()
steve.goto(-400, -50)
steve.pendown()

rick = turtle.Turtle()
rick.color("yellow")
rick.penup()
rick.goto(-400, -100)
rick.pendown()

for i in range(400):
     bob.forward(random.randint(0, 2))
     steve.forward(random.randint(0, 2))
     rick.forward(random.randint(0, 2))


turtle.done()
