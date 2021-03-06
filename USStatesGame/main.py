from turtle import Screen, Turtle
import pandas

def create_turtle(title, position):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.speed(0)
    turtle.goto(position)
    turtle.write(title, align="left", font=("Arial", 10, "normal"))

turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:    
    answer_state = screen.textinput(title=f"Guess the State. {len(guessed_states)}/50 remaining.", prompt="What's another state's name? ").title()

    if answer_state == "Exit":
        for state in df.state:
            if state not in guessed_states:
                states_to_learn.append(state)
        break

    df_state = df[df.state == answer_state]
    if len(df_state) == 1:
        create_turtle(df_state.state.item(), (int(df_state.x), int(df_state.y)))
        guessed_states.append(answer_state)

states_to_learn_df = pandas.DataFrame(states_to_learn)
states_to_learn_df.to_csv("states_to_learn.csv")