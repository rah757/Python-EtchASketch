from turtle import Turtle, Screen

carl = Turtle()
screen = Screen()


def forward():
    carl.fd(10)
def right():
    carl.rt(10)
def back():
    carl.back(10)
def left():
    carl.lt(10)
def clear():
    carl.reset()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=back)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="Escape", fun=clear)
screen.exitonclick()
