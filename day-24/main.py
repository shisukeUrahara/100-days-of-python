from turtle import Turtle, Screen
import time
import random

# ---------------- SCREEN ----------------
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

MOVE_DISTANCE = 20
TICK_MS = 100

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# ---------------- GAME STATE ----------------
game_running = True  # True while snake is moving; False after game over

def get_high_score():
    with open("highscore.txt", "r") as f:
        high_score = f.read()
        return int(high_score)

def update_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


# ---------------- SNAKE ----------------
class Snake:
    def __init__(self):
        self.initiate()

    def initiate(self):
        # remove old segments from screen
        for seg in getattr(self, "segments", []):
            seg.hideturtle()
            seg.goto(1000, 1000)

        self.segments = []
        positions = [(0, 0), (-20, 0), (-40, 0)]
        for pos in positions:
            self.add_segment(pos)
        self.head = self.segments[0]
        self.head.setheading(RIGHT)

    def add_segment(self, position):
        t = Turtle("square")
        t.color("white")
        t.penup()
        t.goto(position[0], position[1])
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


# ---------------- FOOD ----------------
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # grid-aligned food so it matches MOVE_DISTANCE steps
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)


# ---------------- SCOREBOARD ----------------
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.show_top()

    def _draw(self, x, y):
        self.clear()
        self.goto(x, y)
        self.write(
            f"Score {self.score}  HighScore {self.highscore}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def show_top(self):
        self._draw(0, 270)

    def show_center(self):
        self._draw(0, 0)

    def increment_score(self):
        self.score += 1
        self.show_top()

    def game_over(self):
        # update highscore if needed and show at center
        if self.score > self.highscore:
            update_high_score(self.score)
            # self.highscore = self.score

        self.show_center()

    def reset_for_restart(self):
        # score resets to 0, highscore already updated at game over
        self.score = 0
        self.show_top()


snake = Snake()
food = Food()
scoreboard = Scoreboard()


def end_game():
    global game_running
    game_running = False
    scoreboard.game_over()


def tick():
    """One frame of the game."""
    if not game_running:
        screen.update()
        screen.ontimer(tick, TICK_MS)
        return

    snake.move()

    # eat
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        snake.extend()

    # wall collision
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        end_game()

    # tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            end_game()
            break

    screen.update()
    screen.ontimer(tick, TICK_MS)


def restart_game():
    global game_running
    if game_running:
        return  # ignore space during play (optional)

    scoreboard.reset_for_restart()
    food.refresh()
    snake.initiate()
    game_running = True


# controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(restart_game, "space")

tick()
screen.mainloop()
