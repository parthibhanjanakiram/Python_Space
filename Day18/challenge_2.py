from turtle import Screen
import turtle as t
import random

jim = t.Turtle()
t.colormode(255)
jim.shape("arrow")
jim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color


for i in range(72):
    jim.color(random_color())
    jim.circle(75)
    jim.right(5)
    



screen = Screen()
screen.exitonclick()