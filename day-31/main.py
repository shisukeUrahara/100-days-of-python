import os
import random
import tkinter as tk
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Paths relative to this script
images_dir = './images'

# Load words from CSV
df = pd.read_csv('./data/french_words.csv', encoding="utf-8")
words: list[dict] = df.to_dict(orient="records")

# App state
current_word: dict = {}
show_front: bool = True

# Window (must exist before creating PhotoImage)
window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.geometry("400x300")
window.minsize(width=500, height=500)

# Load card and button images (keep references to avoid garbage collection)
card_front_img = tk.PhotoImage(file=os.path.join(images_dir, "card_front.png"))
card_back_img = tk.PhotoImage(file=os.path.join(images_dir, "card_back.png"))
wrong_btn_img = tk.PhotoImage(file=os.path.join(images_dir, "wrong.png"))
right_btn_img = tk.PhotoImage(file=os.path.join(images_dir, "right.png"))

card_w = card_front_img.width()
card_h = card_front_img.height()
card_cx = card_w // 2
card_cy = card_h // 2

# Card canvas: image with title + word on top
card_canvas = tk.Canvas(
    window,
    width=card_w,
    height=card_h,
    bg=BACKGROUND_COLOR,
    highlightthickness=0,
)
card_canvas.pack(pady=(20, 30))

card_image_id = card_canvas.create_image(card_cx, card_cy, image=card_front_img)
# Two-line card: title (e.g. "French") small italic, word large bold
card_title_id = card_canvas.create_text(
    card_cx, card_cy - 50,
    text="",
    font=("Arial", 14, "italic"),
    fill="black",
)
card_word_id = card_canvas.create_text(
    card_cx, card_cy + 20,
    text="",
    font=("Arial", 28, "bold"),
    fill="black",
)

# Buttons frame: red (wrong) and green (right) image buttons
buttons_frame = tk.Frame(window, bg=BACKGROUND_COLOR)
buttons_frame.pack(pady=10)


def flip_card() -> None:
    global show_front
    if not current_word:
        return
    if show_front:
        card_canvas.itemconfig(card_image_id, image=card_back_img)
        card_canvas.itemconfig(card_title_id, text="English")
        card_canvas.itemconfig(card_word_id, text=current_word["English"])
    else:
        card_canvas.itemconfig(card_image_id, image=card_front_img)
        card_canvas.itemconfig(card_title_id, text="French")
        card_canvas.itemconfig(card_word_id, text=current_word["French"])
    show_front = not show_front


def next_card() -> None:
    global current_word, show_front
    if not words:
        card_canvas.itemconfig(card_title_id, text="")
        card_canvas.itemconfig(card_word_id, text="No words loaded")
        return
    current_word = random.choice(words)
    show_front = True
    card_canvas.itemconfig(card_image_id, image=card_front_img)
    card_canvas.itemconfig(card_title_id, text="French")
    card_canvas.itemconfig(card_word_id, text=current_word["French"])


wrong_btn = tk.Button(
    buttons_frame,
    image=wrong_btn_img,
    highlightthickness=0,
    bd=0,
    command=flip_card,
)
wrong_btn.pack(side=tk.LEFT, padx=10)

right_btn = tk.Button(
    buttons_frame,
    image=right_btn_img,
    highlightthickness=0,
    bd=0,
    command=next_card,
)
right_btn.pack(side=tk.LEFT, padx=10)

# Show first card
next_card()

window.mainloop()
