from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1000, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
colors_str = ", ".join(colors)
my_prompt = f"Which will turtle will win the race?\n{colors_str}\nEnter a colour: "
# my_prompt = print(f"Which will turtle will win the race?\n{colors_str}\nEnter a colour: ")
user_bet = screen.textinput(title="Make your bet", prompt=my_prompt)
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            turtle.write("I won the race!!", align="center", font=("Arial", 16, "normal"))
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
