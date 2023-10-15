from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
timmy.width(20)
timmy.speed(7)
timmy.hideturtle()

colors = ['red','black','yellow','blue','orange','green','maroon','purple','beige','brown','navy','gray']
# num_of_sides = 3
# len_of_side = 100

# for c in range (10):

#     angle = 360 / num_of_sides
#     timmy.color(choice(colors))

#     for _ in range(num_of_sides):
#         timmy.forward(len_of_side)
#         timmy.right(angle)

    
#     num_of_sides += 1

angles = [0,90,180,270]

for _ in range(200):

    timmy.setheading(random.choice(angles))
    timmy.forward(30)
    timmy.color(random.choice(colors))










screen = Screen()
screen.exitonclick()