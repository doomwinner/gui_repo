#grid.py

import tkinter as tk
from tkinter import *
import random

root = tk.Tk()
root.title("Sign Up Page")

label_name = tk.Label(root, text="Name:")
label_email = tk.Label(root, text="Email:")
label_password = tk.Label(root, text="Password:")

# Creating entry widgets for user input
entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

# Creating a button for sign up
button_signup = tk.Button(root, text="Sign Up Now")

# Positioning widgets using the grid manager
label_name.grid(row=0, sticky=tk.E)
label_email.grid(row=1, sticky=tk.E)
label_password.grid(row=2, sticky=tk.E)

entry_name.grid(row=0, column=1)
entry_email.grid(row=1, column=1)
entry_password.grid(row=2, column=1)

button_signup.grid(row=3, columnspan=2)

def change_button_font():
    font_family = random.choice(["Arial", "Helvetica", "Times", "Courier", "Comic Sans MS"]) # Random font family
    font_size = random.randint(5, 10) # Random font size between 10 and 20
    font_weight = random.choice(["normal", "bold"]) # Random font weight
    button_signup.config(font=(font_family, font_size, font_weight))
    root.after(500, change_button_font)  # Change font every 500 milliseconds (0.5 seconds)

# Call the function to change font repeatedly
change_button_font()
root.mainloop()
