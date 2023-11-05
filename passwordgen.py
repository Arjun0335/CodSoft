import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length <= 0:
        password_result.set("Please enter a valid length.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_result.set(password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create a label
label = ttk.Label(root, text="Password Length:")
label.pack(pady=10)

# Create an entry field for password length
length_entry = ttk.Entry(root)
length_entry.pack()

# Create a button to generate the password
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create a label to display the generated password
password_result = tk.StringVar()
password_label = ttk.Label(root, textvariable=password_result)
password_label.pack(pady=10)

root.mainloop()
