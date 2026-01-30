import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=500)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = []

# --- Starting positions (left side, different lanes) ---
start_x = -screen.window_width() // 2 + 50
start_y = -150
lane_gap = 60

# --- Finish line (near the right edge) ---
finish_x = screen.window_width() // 2 - 60

# Draw start & finish lines (optional but makes it feel like a race)
line = Turtle()
line.hideturtle()
line.penup()
line.pensize(3)

# Start line
line.goto(start_x - 20, start_y - 30)
line.setheading(90)
line.pendown()
line.forward(lane_gap * (len(colors) - 1) + 60)
line.penup()

# Finish line
line.goto(finish_x, start_y - 30)
line.setheading(90)
line.pendown()
line.forward(lane_gap * (len(colors) - 1) + 60)
line.penup()

# Create racers
for i, c in enumerate(colors):
    t = Turtle("turtle")
    t.color(c)
    t.penup()
    t.setheading(0)  # face right
    t.goto(start_x, start_y + i * lane_gap)
    racers.append(t)

# Ask user for a "bet" (optional fun)
bet = screen.textinput("Turtle Race", f"Who will win? {colors}: ")

# Speed up animation
screen.tracer(0)

race_on = True
winner = None

while race_on:
    for t in racers:
        step = random.randint(1, 12)   # randomness = exciting race
        t.forward(step)

        if t.xcor() >= finish_x:
            race_on = False
            winner = t.pencolor()
            break

    screen.update()

# Announce winner
msg = f"{winner} won!"
if bet:
    msg += " 🎉 You guessed right!" if bet.lower() == winner else f" You guessed {bet}."
print(msg)

screen.exitonclick()

