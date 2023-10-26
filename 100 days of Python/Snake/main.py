from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

snake = Turtle()
snake.shape('square')
snake.color('white')
snake.speed(5)
snake.penup()

snake_tail = []
snake_length = 2

def add_tail():
    tail = Turtle()
    tail.shape('square')
    tail.color('white')
    tail.speed(5)
    tail.penup()
    snake_tail.append(tail)

def up():
    if snake.heading() != 270:
        snake.setheading(90)
 
def down():
    if snake.heading() != 90:
        snake.setheading(270)

def left():
    if snake.heading() != 0:
        snake.setheading(180)

def right():
    if snake.heading() != 180:
        snake.setheading(0)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

playing = True

while playing:

    position = snake.position()
    old_position = snake.position()
    snake.forward(20)
    if snake_length > len(snake_tail):
        add_tail()

    for piece in snake_tail:
        old_position = piece.position()
        piece.goto(position)
        position = old_position







screen.exitonclick()