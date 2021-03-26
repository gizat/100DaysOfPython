from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some text", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.button_true_img = PhotoImage(file="images/true.png")
        self.button_true = Button(image=self.button_true_img, highlightthickness=0)
        self.button_true.grid(column=0, row=2)

        self.button_false_img = PhotoImage(file="images/false.png")
        self.button_false = Button(image=self.button_false_img, highlightthickness=0)
        self.button_false.grid(column=1, row=2)

        self.window.mainloop()