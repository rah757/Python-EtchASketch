from turtle import Turtle, Screen

carl = Turtle()
screen = Screen()


def f():
    carl.fd(10)
def r():
    carl.rt(10)
def b():
    carl.back(10)
def l():
    carl.lt(10)


screen.listen()
screen.onkey(key="space", fun=f)
screen.exitonclick()
