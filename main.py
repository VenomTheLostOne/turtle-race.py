import turtle as t
import random

color_codes = ["red", "orange", "yellow", "green", ]
screen = t.Screen()
screen.setup(500, 400)

red = t.Turtle()
orange = t.Turtle()
yellow = t.Turtle()
green = t.Turtle()
red.color(color_codes[0])
orange.color(color_codes[1])
yellow.color(color_codes[2])
green.color(color_codes[3])
red.shape("turtle")
orange.shape("turtle")
yellow.shape("turtle")
green.shape("turtle")
red.penup()
orange.penup()
yellow.penup()
green.penup()
red.goto(x=-200, y=-100)
orange.goto(x=-200, y=-50)
green.goto(x=-200, y=0)
yellow.goto(x=-200, y=50)
bet = t.textinput("Make your bet", "Which turtle will")
stop = False
while not stop:
    red.forward(random.randint(1, 5))
    if red.pos() == (200, -100):
        stop = True
        print("Red wins!")
        if bet == "red":
            print("You won!")
    orange.forward(random.randint(1, 5))
    if orange.pos() == (200, -50):
        stop = True
        print("orange wins!")
        if bet == "orange":
            print("You won!")
    green.forward(random.randint(1, 5))
    if green.pos() == (200, 0):
        stop = True
        print("Green wins!")
        if bet == "green":
            print("You won!")
    yellow.forward(random.randint(1, 5))
    if yellow.pos() == (200, 50):
        stop = True
        print("Yellow wins!")
        if bet == "yellow":
            print("You won!")
screen.exitonclick()
