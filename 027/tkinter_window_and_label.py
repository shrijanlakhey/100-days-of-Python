# pack(): It is a layout manager which packs each of the widget next to each other in a vaguely logical format. By default, 'pack()' will start from the top and every other widget just below it. It can be changed by adding a 'side' parameter.
import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# places the label on to the screen and automatically centers it
my_label.pack()

# configure or updating the properties of particular component
my_label["text"] = "New text"

# or
# my_label.config(text="New text")

# keeps the window on the screen
window.mainloop()

