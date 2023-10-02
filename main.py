import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("US States")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
guessed_state = []

question = 1

while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"Guess the state: {question}/{len(states_list)}",
        prompt="What's the state's name?",
    ).title()
    if answer_state == None or answer_state == "Exit":
        missing_state = [place for place in states_list if (place not in guessed_state)]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in states_list:
        correct_state = State(
            answer_state,
            float(states_data[states_data["state"] == answer_state]["x"]),
            float(states_data[states_data["state"] == answer_state]["y"]),
        )
        question += 1
        guessed_state.append(answer_state)

# screen.exitonclick()
