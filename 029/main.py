from tkinter import * 
from tkinter import messagebox # since it is another module of code, '*' does not import it so we have to import it separately
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(8, 10))]
    password_symbols = [choice(symbols) for i in range(randint(2, 4))]
    password_numbers = [choice(numbers) for i in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # 'join()' method takes all items in an iterable and joins them into one string. It can also separate the elements using the character given in "". Can join tuple, list or dictionary to a string
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) # automatically copies the password to the clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?") # output is either going to br True or False
        if is_ok:
            with open("029/data.txt", mode="a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="029/logo.png")
canvas.create_image(100, 100, image=logo_img) # x = 100, y = 100
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2) # 'columnspan=2' this entry takes up two columns

# email/username
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)

# defining default email

# here '0' is index, it is baically where the cursor is. If we want to insert the email at the very beginning of the entry, then we can set the value to 0
email_entry.insert(0, "user@gmail.com") 

# alternatively, we can use index 'END' which is a constant which represent the very last character that is inside the entry
# use 'END' if we want to enter something after the text or use '0' to enter something at the beginning of the entry
# email_entry.insert(END, "user@gmail.com")

email_entry.grid(column=1, row=2, columnspan=2) # 'columnspan=2' this entry takes up two columns

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3, sticky="w", padx=3)
password_button = Button(text="Generate", command=generate_password)
password_button.grid(column=2, row=3)

# add
add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()