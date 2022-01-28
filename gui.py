from platform import node
import graph as G
import turtle
from math import sqrt


class Node:
    def __init__(self, num: int, x, y):
        self.id = num
        self.x = x
        self.y = y
        self.NODE_SIZE = 7
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.draw()

    def draw(self):
        self.turtle.goto(self.x, self.y)
        self.turtle.pensize(self.NODE_SIZE)
        self.turtle.dot()
        self.turtle.pensize(1)

    def exist(self, x, y):
        dis = sqrt((self.x-x)**2+(self.y-y)**2)
        if dis < self.NODE_SIZE:
            return True
        return False


turtle.tracer(False)
graph = G.Graph()
head = turtle.Turtle()
ok = turtle.Screen()
head.hideturtle()
head.penup()
ok.delay(None)
count = 0
head.goto(0, 260)
head.write("This is to display the coordinates of the position where mouse is clicked",
           align="center")


def btnclick(x, y):
    global count
    count += 1
    head.clear()
    head.write(f"x coordinate = {x}, y coordinate = {y}", align="center")
    graph.addNode(Node(count, x, y))
    turtle.update()


turtle.onscreenclick(btnclick, 1, True)
turtle.listen()
turtle.done()
