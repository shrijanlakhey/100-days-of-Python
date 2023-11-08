# grid(): It is a layout manager which imagines that the entire program is a grid and we can divide it into any number of columns and rows as we want.
# It is relative to other components
# first row = 0 and first column = 0
from tkinter import *

def button_clicked():
   new_text = input.get()
   my_label["text"] = new_text
 
window = Tk()
window.title("Entry in tkinter")
window.minsize(width=500,height=300)
# adding padding to the entire window
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
# adding padding to a specific widget
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Change text", command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="New Button", command=button_clicked)
new_button.grid(column=2,row=0)
    
# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)




# keeps the window on the screen
window.mainloop()