from turtle import Turtle

FONT = ("Arial", 10, "bold")


class State(Turtle):
    def __init__(self, state, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(state, align="center", font=FONT)
