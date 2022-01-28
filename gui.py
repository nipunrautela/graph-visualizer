from time import time

from graph import Graph
import turtle
from math import sqrt


class Stats:
    def __init__(self):
        self.count = 0
        self.last_update = time()
        self.head = turtle.Turtle()
        self.head.hideturtle()

    def show_fps(self):
        self.count += 1
        self.head.pu()
        self.head.clear()
        fps = round(self.count / (time() - self.last_update + 1), 2)
        self.head.goto(-470, 380)
        self.head.write(str(fps), True, font=('Arial', 10, 'normal'))


class Node:
    id = 0
    NODE_SIZE = 12

    def __init__(self, x, y, tur):
        self.id = Node.id
        Node.id += 1
        self.x = x
        self.y = y
        self.selected = False

        self.turtle = tur
        self.turtle.penup()
        self.draw()

    def draw(self):
        if self.selected:
            self.turtle.color("green")
        else:
            self.turtle.color("white")

        self.turtle.goto(self.x, self.y)
        self.turtle.pensize(Node.NODE_SIZE)
        self.turtle.dot()
        self.turtle.pensize(1)

    def exist(self, x, y):
        dis = sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        if dis < Node.NODE_SIZE:
            return True
        return False


class Edge:
    EDGE_SIZE = 3

    def __init__(self, n1: Node, n2: Node, tur):
        self.n1 = n1
        self.n2 = n2
        self.selected = False

        self.turtle = tur
        self.draw()

    def draw(self):
        if self.selected:
            self.turtle.color("green")
        else:
            self.turtle.color("black")

        self.turtle.pensize(Edge.EDGE_SIZE)
        self.turtle.pu()
        self.turtle.goto(self.n1.x, self.n1.y)
        self.turtle.pd()
        self.turtle.goto(self.n2.x, self.n2.y)

    def exist(self, x, y):
        try:
            m = (self.n2.y - self.n1.y) / (self.n2.x - self.n1.x)
        except ZeroDivisionError:
            m = (self.n2.y - self.n1.y) / float("-inf")
        a = m
        b = -1
        c = self.n1.y - (m * self.n1.x)

        distance = (a * x + b * y + c) / sqrt(a ** 2 + b ** 2)
        if distance < Edge.EDGE_SIZE:
            return True
        return False


class GraphGui:
    def __init__(self, screen):
        self.graph = Graph()
        self.nodes = {}
        self.edges = {}

        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.screen = screen

        self.selected_node = None
        self.selected_edge = None

        self.stats = Stats()

    def _create_node(self, x, y):
        new_node = Node(x, y, self.turtle)
        self.graph.addNode(new_node.id)
        self.nodes[new_node.id] = new_node
        return new_node.id

    def _create_edge(self, n1, n2):
        new_edge = Edge(n1, n2, self.turtle)
        self.graph.addEdge(n1.id, n2.id)
        self.edges[str(n1.id) + ',' + str(n2.id)] = new_edge

    def on_left_click(self, x, y):
        clicked_node = None

        for k in self.nodes.keys():
            if self.nodes[k].exist(x, y):
                clicked_node = k
        if clicked_node is None:
            node_id = self._create_node(x, y)
            if self.selected_node is not None:
                self.nodes[self.selected_node].selected = False
            self.selected_node = node_id
            self.nodes[node_id].selected = True
        else:
            if clicked_node == self.selected_node:
                self.nodes[clicked_node].selected = False
                self.selected_node = None
            else:
                if self.selected_node is not None:
                    self.nodes[self.selected_node].selected = False
                self.nodes[clicked_node].selected = True
                self.selected_node = clicked_node

        clicked_edge = None

        for k in self.edges.keys():
            if self.edges[k].exist(x, y):
                clicked_edge = True
                if self.edges[k] is self.selected_edge:
                    self.edges[k].selected = False
                    self.edges[self.selected_edge].selected = False
                    self.selected_edge = None
                else:
                    self.edges[k].selected = True
                    self.selected_edge = k

    def draw(self):
        turtle.update()
        self.turtle.clear()
        self.stats.show_fps()
        turtle.ontimer(self.draw, 20)
        for k in self.nodes.keys():
            self.nodes[k].draw()
        for k in self.edges.keys():
            self.edges[k].draw()


def main():
    turtle.tracer(False)
    turtle.hideturtle()
    screen = turtle.getscreen()
    turtle.screensize(800, 800)
    screen.bgcolor("grey")

    gui = GraphGui(screen)
    screen.listen()
    turtle.onscreenclick(gui.on_left_click, 1, True)
    gui.draw()

    turtle.done()


main()
