import turtle
import pandas

screen = turtle.Screen()
screen.title("American states")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed = []
while len(guessed) < 50:
    ans_state = screen.textinput(title=f"{len(guessed)}/50 correct", prompt="whats another state").title()
    print(ans_state)

    if ans_state in all_states:
        guessed.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(ans_state)

screen.exitonclick()