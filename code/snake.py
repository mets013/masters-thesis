"a snake game"

import turtle
import time
import random

# Set up screen
WIN = turtle.Screen()
WIN.title("Snake Game")
WIN.bgcolor("black")
WIN.setup(width=600, height=600)
WIN.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake body
segments = []


# Functions
def go_up():
    """ go up """
    if head.direction != "down":
        head.direction = "up"


def go_down():
    """ go down """
    if head.direction != "up":
        head.direction = "down"


def go_left():
    """ go left """
    if head.direction != "right":
        head.direction = "left"


def go_right():
    """" go right """
    if head.direction != "left":
        head.direction = "right"


def move():
    """ move """
    if head.direction == "up":
        local_y = head.ycor()
        head.sety(local_y + 20)

    if head.direction == "down":
        local_y = head.ycor()
        head.sety(local_y - 20)

    if head.direction == "left":
        local_x = head.xcor()
        head.setx(local_x - 20)

    if head.direction == "right":
        local_x = head.xcor()
        head.setx(local_x + 20)


# Keyboard bindings
WIN.listen()
WIN.onkeypress(go_up, "w")
WIN.onkeypress(go_down, "s")
WIN.onkeypress(go_left, "a")
WIN.onkeypress(go_right, "d")

# Main game loop
while True:
    WIN.update()

    # Check border collision
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    # Check food collision
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Add segment to snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move snake segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check head and body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(0.1)
