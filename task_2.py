from random import randint
from turtle import exitonclick, forward, left, penup, pendown, back

inflacja = 15

def rectangle(a,b):
    for _ in range(2):
        forward(a)
        left(90)
        forward(b)
        left(90)

penup()
back(100)
pendown()
for _ in range(20):
    rectangle(15,inflacja)
    penup()
    forward(20)
    pendown()
    inflacja += randint(-10,30)

exitonclick()
