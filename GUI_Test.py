#!/usr/bin/env python

import tkinter as tk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.configure(text="Result: " + str(result))
    except ValueError:
        result_label.configure(text="Invalid input!")

# Create the main window
window = tk.Tk()
window.title("Add Numbers")

# Create input labels and entry fields
label1 = tk.Label(window, text="Number 1:")
label1.pack()
entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Number 2:")
label2.pack()
entry2 = tk.Entry(window)
entry2.pack()

# Create the add button
add_button = tk.Button(window, text="Add", command=add_numbers)
add_button.pack()

# Create the result label
result_label = tk.Label(window, text="Result:")
result_label.pack()

# Start the GUI event loop
window.mainloop()
