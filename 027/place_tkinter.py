# place(): It is a layout manager which is all about precise postioning. We can provide X and Y value when we place something
from tkinter import *

def button_clicked():
   new_text = input.get()
   my_label["text"] = new_text
 
window = Tk()
window.title("Entry in tkinter")
window.minsize(width=500,height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=100,y=200)


# keeps the window on the screen
window.mainloop()