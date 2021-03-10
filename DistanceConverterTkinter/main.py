from tkinter import * 


def button_clicked():
    mi = float(input.get())
    mi_to_km = mi * 1.60934
    output_label["text"] = mi_to_km


window = Tk()
window.title("Mi to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=10, pady=10)

input = Entry(width=5)
input.grid(column=1, row=0)

mi_label = Label(text="miles", font=("Arial", 12))
mi_label.grid(column=2, row=0)
mi_label.config(padx=20, pady=20)

equals_label = Label(text="is equal to", font=("Arial", 12))
equals_label.grid(column=0, row=1)

output_label = Label(text="0", font=("Arial", 12))
output_label.grid(column=1, row=1)

km_label = Label(text="km", font=("Arial", 12))
km_label.grid(column=2, row=1)
    
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# This loop has to be at the end of the program
window.mainloop()