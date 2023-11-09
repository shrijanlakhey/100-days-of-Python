from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer) # canceling the timer
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60  

    # dynamic typing allows the type of data to be determined during program execution meaning a variable can either hold integer or string value
    if count_sec < 10:
        count_sec = f"0{count_sec}" # here the 'count_sec' variable originally holded an integer but its content is changed to a string


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1) # after 1000 ms delay the output will be displayed. 'count - 1' is an argument which will be passed to the 'count_down' function
    else:
        start_timer() # when the count goes to 0, this will trigger the timer to count start countig again
        marks = ""
        # since we have 4 work sessions and four breaks, we can divide the reps by 2 to get total number of work sessions so that a checkmark can be added everytime a work session is completed
        work_sessions = math.floor(reps/2) 

        for i in range(work_sessions):
            marks += "✔"
            checkmarks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)

# canvas widget allows us to layer things one on top of the other
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) # height and width are measured in pixels. 'highlightthickness' determines the thickness of the border
tommato_img = PhotoImage(file="028/tomato.png")
canvas.create_image(100, 112, image=tommato_img) # x = 100, y = 112
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",bg="white", bd=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",bg="white", bd=0, command=reset_timer)
reset_button.grid(column=2, row=2)

checkmarks = Label(fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)


window.mainloop()