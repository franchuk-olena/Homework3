import turtle
from random import randint, random

class Triangle:
    def __init__(self, size, x, y):
        self.size = size
        self.color = (random(), random(), random())
        self.x = x
        self.y = y

    def set_color(self, color):
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()

        turtle.fillcolor(self.color)
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(self.size)
            turtle.left(120)
        turtle.end_fill()


def main():
    turtle.speed(0)
    turtle.hideturtle()

    for i in range(100):
        x = randint(-300, 300)
        y = randint(-300, 300)
        triangle = Triangle(randint(50, 200), x, y)
        triangle.draw()

    turtle.done()

if __name__ == "__main__":
    main()
