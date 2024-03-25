#place.py

import tkinter as tk
from tkinter import *

# Creating the main window
root = tk.Tk()
root.title("Login Page")

# Creating labels for Username and Password
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")

# Creating entry widgets for user input
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

# Creating a button for login
button_login = tk.Button(root, text="Login")

# Placing widgets using the place manager
label_username.place(x=10, y=10)
label_password.place(x=10, y=40)

entry_username.place(x=80, y=10)
entry_password.place(x=80, y=40)

button_login.place(x=100, y=70)

root.mainloop()
