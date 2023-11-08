from tkinter import *

window = Tk()
window.title("Entry in tkinter")
window.minsize(width=500,height=300)

# Label
my_label = Label(text="Type below to change text", font=("Arial", 24, "bold"))
# places the label on to the screen and automatically centers it
my_label.pack()



# Entry (basically just input)

input = Entry(width=10)
input.pack()
input.get() # 'get()' method returns the input given by the user as a string



# Button

def button_clicked():
   new_text = input.get()
   my_label["text"] = new_text

button = Button(text="Change text", command=button_clicked) # 'command' takes the name of a function not calling of the function, so '()' are not required
button.pack()
    





# keeps the window on the screen
window.mainloop()