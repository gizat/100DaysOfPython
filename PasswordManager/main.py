from tkinter import *

FONT_NAME = "Arial"
FONT_SIZE = 14

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

entry_email = Entry(width=35, highlightthickness=0, bg="white")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=19, highlightthickness=0, bg="white")
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate password", highlightthickness=0, bg="white", width=12)
button_generate.grid(column=2, row=3)

button_add = Button(text="Add", highlightthickness=0, width=32, bg="white")
button_add.grid(column=1, row=4, columnspan=2)









window.mainloop()