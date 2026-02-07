import turtle
import pandas


screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.title("US States Game")
image= 'blank_states_img.gif'
Turtle= turtle.Turtle
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)

# answer_state= screen.textinput(title= "Us states game",prompt="Guess a state")
# print(answer_state)

import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

score = 0
guessed_states = set()

def write_state_name(name, x, y):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.color("black")
    writer.write(name, align="center", font=("Arial", 8, "normal"))

while score < 50:
    answer_state = screen.textinput(
        title=f"{score}/50 States Correct",
        prompt="Guess a state (or Cancel to quit)"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state in guessed_states:
        continue

    match = data[data["state"] == answer_state]
    if not match.empty:
        row = match.iloc[0]
        write_state_name(row["state"], int(row["x"]), int(row["y"]))
        guessed_states.add(answer_state)
        score += 1

turtle.mainloop()


# screen.exitonclick()