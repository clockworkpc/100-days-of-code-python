"""Day 18: Turtle Graphics"""

import turtle as turtle_module
import sys


class MyTurtle:
    def __init__(self):
        self.t = turtle_module.Turtle()
        self.canvas = self.t.getscreen().getcanvas()
        # self.screen = self.set_up_screen()

    def set_up_screen(self, width=600, height=600, bgcolor="white"):
        screen = turtle_module.Screen()
        screen.setup(width=600, height=600)
        screen.bgcolor("white")
        return screen

    def draw_square(self):
        for _ in range(4):
            self.t.forward(100)
            self.t.left(90)

    def draw_dashed_line(self):
        for _ in range(15):
            self.t.forward(10)
            self.t.penup()
            self.t.forward(10)
            self.t.pendown()


def main():
    g = MyTurtle()

    if sys.argv[1] in dir(g):
        getattr(g, sys.argv[1])()
    else:
        print(f"Turtle cannot do this: {sys.argv[1]}")


if __name__ == "__main__":
    main()
