import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        # Create entry field for calculator
        self.entry = tk.Entry(master, width=25, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons for calculator
        button_text = [
            "7", "8", "9", "/", "sin",
            "4", "5", "6", "*", "cos",
            "1", "2", "3", "-", "tan",
            "0", ".", "pi", "+", "sqrt",
            "(", ")", "Clear", "=", "log",
        ]

        self.buttons = []
        for i in range(len(button_text)):
            button = tk.Button(master, text=button_text[i], width=5, height=2,
                               font=("Arial", 12), command=lambda x=button_text[i]: self.button_click(x))
            self.buttons.append(button)
            row = i // 5 + 1
            col = i % 5
            button.grid(row=row, column=col, padx=3, pady=3)

    def button_click(self, text):
        if text == "Clear":
            self.entry.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "pi":
            self.entry.insert(tk.END, str(math.pi))
        elif text == "sin":
            try:
                result = math.sin(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "cos":
            try:
                result = math.cos(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "tan":
            try:
                result = math.tan(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "sqrt":
            try:
                result = math.sqrt(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        elif text == "log":
            try:
                result = math.log10(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, text)

# Create the GUI window and start the program
root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
