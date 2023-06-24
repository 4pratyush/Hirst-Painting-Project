import turtle as t
import random

import color_extraction

color_list = color_extraction.rgb_colors
tim = t.Turtle()
tim.penup()
tim.speed("fastest")
screen = t.Screen().bgcolor("black")

t.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for x in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.right(180)

screen.exitonclick()



