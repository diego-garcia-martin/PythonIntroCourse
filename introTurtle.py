import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Turtle()
# turtle.bgcolor('black')
# for x in range(360):
#     t.color(colors[x%6])
#     t.width(x/100 + 1)
#     t.forward(x)
#     t.left(58)

turtle.bgcolor("black")
turtle.screensize(800, 400)

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

bob.forward(800)
steve.forward(800)
rick.forward(800)

turtle.done()