import turtle
import time
import random

class Paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape("square")
        self.t.color("white")
        self.t.penup()
        self.t.goto(x, y)
        self.t.shapesize(stretch_wid=5, stretch_len=1)
    def move_up(self):
        self.y = min(self.y + 20, 250)
        self.t.sety(self.y)
    def move_down(self):
        self.y = max(self.y - 20, -250)
        self.t.sety(self.y)


class Ball():
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.shape("square")
        self.t.color("white")
        self.t.penup()
        self.t.goto(x, y)

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.t.setx(self.x)
        self.t.sety(self.y)
        if self.y > 290 or self.y < -290:
            self.dy *= -1

    def reset(self):
        self.x = 0
        self.y = 0
        self.t.setx(self.x)
        self.t.sety(self.y)
        self.dy = random.randint(1, 8)
        self.dx *= -1
    

class Score():
    scoreA = 0
    scoreB = 0
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.hideturtle()
    pen.goto(0, 260)
    
    def write(self):
        self.pen.clear()
        self.pen.write(f"Player1: {self.scoreA}  Player2: {self.scoreB}", align="center", font=("Courier", 25, "normal"))


class Game():
    window = turtle.Screen()
    window.title("Pong Game")
    window.bgcolor("black")
    window.setup(width=800, height=600)
    window.tracer(0)

    paddleA = Paddle(-350, 0)
    paddleB = Paddle(350, 0)
    ball = Ball(0, 0, 4, 2)
    score = Score()

    s_time = 0.015

    def __init__(self):
        self.window.listen()
        self.window.onkeypress(self.paddleA.move_up, "w")
        self.window.onkeypress(self.paddleA.move_down, "s")
        self.window.onkeypress(self.paddleB.move_up, "Up")
        self.window.onkeypress(self.paddleB.move_down, "Down")

    def check_collision(self):
        if self.ball.x < -340 and self.ball.x > -350:
            if self.ball.y < self.paddleA.y + 30 and self.ball.y > self.paddleA.y - 30:
                self.ball.dx *= -1
                self.s_time = max(0, self.s_time - 0.001)
            if self.ball.y < self.paddleA.y + 60 and self.ball.y > self.paddleA.y + 30:
                self.ball.dy += 2
                self.ball.dx *= -1
                self.s_time = max(0, self.s_time - 0.001)
            if self.ball.y < self.paddleA.y - 30 and self.ball.y > self.paddleA.y - 60:
                self.ball.dx *= -1
                self.ball.dy -= 2
                self.s_time = max(0, self.s_time - 0.001)
        if self.ball.x > 340 and self.ball.x < 350:
            if self.ball.y < self.paddleB.y + 30 and self.ball.y > self.paddleB.y - 30:
                self.ball.dx *= -1
                self.s_time = max(0, self.s_time - 0.001)
            if self.ball.y < self.paddleB.y + 60 and self.ball.y > self.paddleB.y + 30:
                self.ball.dy += 2
                self.ball.dx *= -1
                self.s_time = max(0, self.s_time - 0.001)
            if self.ball.y < self.paddleB.y - 30 and self.ball.y > self.paddleB.y - 60:
                self.ball.dx *= -1
                self.ball.dy -= 2
                self.s_time = max(0, self.s_time - 0.001)
        if self.ball.x > 390:
            self.ball.reset()
            self.s_time = 0.01
            self.score.scoreA += 1
        if self.ball.x < -390:
            self.ball.reset()
            self.s_time = 0.01
            self.score.scoreB += 1
    
    def update(self):
        self.window.update()
        self.ball.update()
        self.check_collision()
        self.score.write()
        time.sleep(self.s_time)


game = Game()

while True:
    game.update()