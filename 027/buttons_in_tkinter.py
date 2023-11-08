import tkinter

window = tkinter.Tk()
window.title("Buttons in tkinter")
window.minsize(width=500,height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# places the label on to the screen and automatically centers it
my_label.pack()


# configure or updating the properties of particular component
my_label.config(text="New text")



# Button

# def button_clicked():
#     print("I got clicked")

def button_clicked():
   my_label["text"] = "Button got clicked"

button = tkinter.Button(text="Click Me", command=button_clicked) # 'command' takes the name of a function not calling of the function, so '()' are not required
button.pack()
    

# keeps the window on the screen
window.mainloop()