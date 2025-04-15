from turtle import Turtle,Screen
import random

my_turtle = Turtle()
my_turtle.shape('turtle')

colors = ["blue", "midnight blue", "cyan", "lime green", "lemon chiffon", "goldenrod", "orange red", "blue violet", "sienna", "dark turquoise"]

def shape_sides(no_of_sides):
    angle = 360/no_of_sides
    
    for i in range(no_of_sides):
        my_turtle.forward(75)
        my_turtle.right(angle)
        
for j in range(3,11):
    my_turtle.color(random.choice(colors))
    shape_sides(j)

screen = Screen()
screen.exitonclick() 

