from turtle import Turtle, Screen, colormode
import random

timmy = Turtle(visible=False)
timmy.width(2)
timmy.speed(100)


colormode(255)

def random_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))


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

# angles = [0,90,180,270]

# for _ in range(5000):

#     timmy.setheading(random.choice(angles))
#     timmy.forward(30)
#     timmy.color()

radius = 150
angle =  5
for _ in range(int(360/angle)):
    timmy.circle(radius)
    timmy.left(angle)
    timmy.color(random_color())



screen = Screen()
screen.exitonclick()