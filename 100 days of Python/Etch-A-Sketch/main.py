from turtle import Turtle, Screen, clear

tim = Turtle()
tim.speed('fastest')
screen = Screen()

# KEY PARAMS

TIM_SPEED = 10
TIM_TURN = 10

def move_forward():
    tim.forward(TIM_SPEED)

def move_backward():
    tim.back(TIM_SPEED)

def turn_left():
    tim.left(TIM_TURN)

def turn_right():
    tim.right(TIM_TURN)

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=turn_left)
screen.onkeypress(key='d', fun=turn_right)
screen.onkeypress(key='c', fun=tim.clear)
screen.exitonclick()