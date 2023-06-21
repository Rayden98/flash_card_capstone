from tkinter import *
from tkinter import messagebox
import pandas
import random
import functools

# ------------------------------------ CONSTANTS ------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
BLACK_COLOR = "#000000"
WHITE_COLOR = "#FFFFFF"

random_word = None

# ------------------------- CREATING A NEW FLASH CARD --------------------------#

data = pandas.read_csv("./data/french_words.csv")
dictionary = data.to_dict(orient="records")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(dictionary1)
    canvas.itemconfig(card_background, image=logo_img2)

    canvas.itemconfig(card_title, text="French", fill=BLACK_COLOR)
    canvas.itemconfig(card_word, text=random_word["French"], fill=BLACK_COLOR)

    # flip_card1 = flip_card(random_word)

    flip_timer = window.after(3000, flip_card)
    print("it's done next card")


def flip_card():
    canvas.itemconfig(card_title, text="English", fill=WHITE_COLOR)
    canvas.itemconfig(card_word, text=f"{random_word['English']}", fill=WHITE_COLOR)
    canvas.itemconfig(card_background, image=logo_img1)


def erase_card():
    global dictionary, random_word

    dictionary.remove(random_word)

    df = pandas.DataFrame.from_dict(dictionary)
    print(df)
    df.to_csv("word_to_learn.csv", sep=',', index=False, encoding='utf-8')
def combine_function():
    next_card()
    erase_card()


# ---------------------------------- UI ---------------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(300, flip_card)
# Background Green
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img1 = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=logo_img1)
canvas.grid(column=0, row=1, columnspan=2)

# Background White
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img2 = PhotoImage(file="./images/card_front.png")
card_front = canvas.create_image(400, 263, image=logo_img2)
canvas.grid(column=0, row=1, columnspan=2)

# Labels
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

# Buttons
image_wrong = PhotoImage(file="./images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(column=0, row=2)

image_right = PhotoImage(file="./images/right.png")
button_wrong = Button(image=image_right, highlightthickness=0, command=combine_function)
button_wrong.grid(column=1, row=2)

# ------------------------- COMING BACK THE DATA ------------------------------#
try:
    data_to_learn = pandas.read_csv("word_to_learn.csv")
    print("It's done")
    dictionary1 = data_to_learn.to_dict(orient="records")
    next_card()
    dictionary = dictionary1

except:
    df = pandas.DataFrame.from_dict(dictionary)
    print(df)
    df.to_csv("word_to_learn.csv", sep=',', index=False, encoding='utf-8')

    dictionary1 = df.to_dict(orient="records")
    next_card(dictionary1)

mainloop()
