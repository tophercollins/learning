# Color Setup

import colorgram

colors = colorgram.extract('100 days of Python/Dots/dots.jpg',42)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

# Key Values

circle_size = 10
num_of_circ_row = 10
num_of_circ_col = 10
separation = 20
screen_width =  200
screen_height =  200
starting_x = -(screen_width)
starting_y = -(screen_height)



import turtle as t

screen = t.Screen()
t.screensize(screen_width,screen_height)

timmy = t.Turtle(visible=False)
timmy.shape(None)
timmy.penup()
timmy.setx(starting_x)
timmy.sety(starting_y)
timmy.pendown()
timmy.width(2)
timmy.speed(100)
t.colormode(255)



def draw_cicle():
    timmy.color(rgb_colors[15])
    timmy.fillcolor(rgb_colors[15])
    timmy.begin_fill()
    timmy.circle(50)
    timmy.end_fill()

draw_cicle()




screen.exitonclick()