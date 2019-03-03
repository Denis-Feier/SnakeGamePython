import turtle
import os
import random
import time

delay = 0.1

score = 0
high_score = 0

screen =turtle.Screen()
screen.bgcolor('red')
screen.setup(width=600, height=600)
screen.title('Snake Game in Python')
screen.tracer(0)

snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('blue')
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'


food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('black')
food.penup()
food.goto(100, 100)

segment = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0 High Score 0', align='center', font=('Courier', 24, 'normal'))

def go_up():
    if snake.direction != 'down':
        snake.direction = 'up'


def go_down():
    if snake.direction != 'up':
        snake.direction = 'down'


def go_left():
    if snake.direction != 'right':
        snake.direction = 'left'


def go_right():
    if snake.direction != 'left':
        snake.direction = 'right'


def move():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 15)

    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 15)

    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 15)

    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 15)


screen.listen()
screen.onkeypress(go_up, 'w')
screen.onkeypress(go_down, 's')
screen.onkeypress(go_left, 'a')
screen.onkeypress(go_right, 'd')

while True:
    screen.update()

    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        time.sleep(2)
        snake.goto(0, 0)
        snake.direction = 'stop'

        for seg in segment:
            seg.goto(1000, 1000)

        segment.clear()

        score = 0

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center',
                  font=('Courier', 24, 'normal'))

    if snake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('grey')
        new_segment.penup()
        segment.append(new_segment)

        score += 1

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align='center', font=('Courier', 24, 'normal'))

    for index in range(len(segment) - 1, 0, -1):
        x = segment[index - 1].xcor()
        y = segment[index - 1].ycor()
        segment[index].goto(x, y)

    if len(segment) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segment[0].goto(x, y)

    move()

    for seg in segment:
        if seg.distance(snake) < 5:
            time.sleep(2)
            snake.goto(0, 0)
            snake.direction = 'stop'

            for se in segment:
                se.goto(1000, 1000)

            segment.clear()

            score = 0

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align='center',
                      font=('Courier', 24, 'normal'))

    time.sleep(delay)
