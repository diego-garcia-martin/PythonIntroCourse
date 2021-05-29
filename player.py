import turtle
import random

class Player():
    def __init__(self, name, color, x, y):
        self.name = name
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.speed(10)
        self.x = x
        self.y = y
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

    def move(self):
        movement = random.randint(0, 5)
        self.t.forward(movement)
        self.x += movement