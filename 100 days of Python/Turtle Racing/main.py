from turtle import Turtle, Screen
import random

screen = Screen()
WIDTH = 500
HEIGHT = 400
screen.setup(width=WIDTH,height=HEIGHT)
user_bet = screen.textinput("Make your bet!", "Which turtle will win? Enter a color:")

colors = ['red','orange','yellow','green','blue','purple']
turtles = []
y_separation = int(HEIGHT/len(colors))-10
y_pos = y_separation/2-(3*y_separation)

for color in colors:

    turtles.append(Turtle(shape='turtle'))
    turtles[-1].color(color)
    turtles[-1].penup()
    turtles[-1].goto((-230,y_pos))
    turtles[-1].pendown()
    y_pos += y_separation


is_race_on = False

def random_distance():
    return random.randint(0,10)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        turtle.forward(random_distance())
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner.lower() == user_bet.lower():
                print(f'You win! The winning color is {winner}!')
            else:
                print(f'You lost! The winning color is {winner}!')

    

screen.listen()

screen.exitonclick()