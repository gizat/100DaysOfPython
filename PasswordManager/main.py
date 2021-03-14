from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

FONT_NAME = "Arial"
FONT_SIZE = 14
DEFAULT_EMAIL = "gizat@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters= [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    entry_password.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            entry_password.delete(0, END)
            entry_email.delete(0, END)
            entry_email.insert(END, DEFAULT_EMAIL)
            entry_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="white")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg="white")
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = locker_img)
canvas.grid(column=0, row=0, columnspan=3)

title_website = Label(text="Website:", font=(FONT_NAME, FONT_SIZE), bg="white", highlightthickness=0)
title_website.grid(column=0, row=1)

title_email = Label(text="Email:", font=(FONT_NAME, FONT_SIZE), bg="white", highlightthickness=0)
title_email.grid(column=0, row=2)

title_password = Label(text="Password:", font=(FONT_NAME, FONT_SIZE), bg="white", highlightthickness=0)
title_password.grid(column=0, row=3)

entry_website = Entry(width=35, highlightthickness=0, bg="white")
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()

entry_email = Entry(width=35, highlightthickness=0, bg="white")
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(END, DEFAULT_EMAIL)

entry_password = Entry(width=19, highlightthickness=0, bg="white")
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate password", highlightthickness=0, bg="white", width=12, command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", highlightthickness=0, width=32, bg="white", command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()