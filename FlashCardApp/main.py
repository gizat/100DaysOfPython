from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")

df = pandas.read_csv("data/french_words.csv")
data_dict = df.to_dict(orient="records")


def next_card():
    random_word = choice(data_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=random_word["French"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image = card_front_image)
card_title = canvas.create_text(400, 150, text="Title", font=FONT_TITLE)
card_word = canvas.create_text(400, 263, text="Word", font=FONT_WORD, tag="word_tag")
canvas.grid(column=0, row=0, columnspan=2)

button_right_img = PhotoImage(file="images/right.png")
button_right = Button(image=button_right_img, highlightthickness=0, command=next_card)
button_right.grid(column=1, row=1)

button_wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=button_wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=1)

next_card()

window.mainloop()
