# Este es ideal para comenzar a usar objetos de clases
import turtle
import random

class Corredor():
    def __init__(self, y, color):
        self.t = turtle.Turtle()
        self.t.speed(0.1)
        self.t.penup()
        self.t.goto(-400, y)
        self.t.color(color)
        self.t.pendown()
        

window = turtle.Screen()
window.bgcolor("black")
window.title("Carrera de Tortugas")
window.setup(width=1000, height=400)

red = Corredor(50, "red")
yellow = Corredor(0, "yellow")
blue = Corredor(-50, "blue")
pink = Corredor(-20, "pink")
white = Corredor(20, "white")

while red.t.xcor() < 400 and yellow.t.xcor() < 400 and blue.t.xcor() < 400 and white.t.xcor() < 400 and pink.t.xcor() < 400:
    red.t.forward(random.randint(0, 5))
    yellow.t.forward(random.randint(0, 5))
    blue.t.forward(random.randint(0, 5))
    white.t.forward(random.randint(0, 5))
    pink.t.forward(random.randint(0, 5))

turtle.done()