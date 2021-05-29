import turtle
import random
import player


turtle.bgcolor("black")
turtle.screensize(800, 400) # de -400 a 400 en x y de -200 a 200 en y


bob = player.Player("Bob", "blue", -400, -200)
joe = player.Player("Joe", "red", -400, 0)
susan = player.Player("Susan", "pink", -400, 200)


for i in range(1000):
    bob.move()
    joe.move()
    susan.move()
    if bob.x > 100:
        print(f"{bob.name} es el ganador!!!")
        break
    if joe.x > 100:
        print(f"{joe.name} es el ganador!!!")
        break
    if susan.x > 100:
        print(f"{susan.name} es el ganador!!!")
        break

turtle.done()