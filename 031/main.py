from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# CSV file
try:
    data = pandas.read_csv("031/data/words_to_learn.csv")
except FileNotFoundError:
    origna_data = pandas.read_csv("031/data/korean_words.csv")
    to_learn = origna_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    """displays a Korean word"""
    global current_card, flip_timer
    # 'after_cancel()': cancels or stop a particular schedule of a callback function
    window.after_cancel(flip_timer) 
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text = "Korean", fill = "black")
    canvas.itemconfig(card_word, text = current_card["Korean"], fill = "black")
    canvas.itemconfig(card_background,image = card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    """displays an English translation of the Korean word"""
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background,image = card_back_image)

def known_words():
    """removes the words known by the user from the dictionary and creates a new CSV file consisting of the words that the user doesn't know"""
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv("031/data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.configure(bg=BACKGROUND_COLOR, padx=50, pady=50)

# 'after()': calls the callback function once after a delay milliseconds (ms) within Tkinter's main loop
# 'callback function' : function that is passed to another function as an argument (here flip_card is a callback function)
flip_timer = window.after(5000, func=flip_card)

#Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="031/images/card_front.png")
card_back_image = PhotoImage(file="031/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image) # x = 400, y = 263 (halving the width and heighto of the canvas as the image needs to be in the center)
card_title = canvas.create_text(400, 150, text= "Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="031/images/wrong.png")
unknown_button = Button(image=wrong_image, bd=0,command=next_card)
unknown_button.grid(column=0, row=1)

right_image = PhotoImage(file="031/images/right.png")
known_button = Button(image=right_image, bd=0, command=known_words)
known_button.grid(column=1, row=1)

# calling this method so that the 'Title' and 'Word' will be replaced by 'Korean' and a korean word after all the images, texts and buttons have been created
# window.after_cancel(id=next_card)
next_card()
# window.after(3000, next_card_eng)

window.mainloop()
