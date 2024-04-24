"""Day 25: CSV and Panda US States Game"""

import turtle
import pandas

assets = "src/days_of_code/assets"
screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{assets}/images/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv(f"{assets}/csv/50_states.csv")
all_states = data.myState.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    )
    answer_state = answer.title() if answer else "Exit"
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.myState == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
