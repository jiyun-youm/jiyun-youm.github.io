from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput("make your bet", "which turtle will win the race? enter a code: ")
colors=["red","orange","yellow","green","blue","purple"]

is_race_on=False
turtles=[]
for color in colors:
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-230, colors.index(color) * 45 - 100)
    turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_bet:
                print(f"you've won! the {winning_color} is the winner")
            else:
                print(f"you lost! the {winning_color} is the winner")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()