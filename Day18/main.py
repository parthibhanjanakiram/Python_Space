from turtle import Turtle,Screen

my_turtle = Turtle()
my_turtle.shape('turtle')
t=100
for i in range(4):
    my_turtle.forward(t)
    my_turtle.left(90)



screen = Screen()
screen.exitonclick()  # Window closes when you click it