import tkinter as tk
from tkinter import ttk

def generate_table():
    """Generates and displays the multiplication table."""
    try:
        num = int(number_entry.get())
        up_to = int(range_entry.get()) if range_entry.get() else 10
        result_text.set("\n".join([f"{num} x {i} = {num * i}" for i in range(1, up_to + 1)]))
    except ValueError:
        result_text.set("Please enter valid numbers!")

# Create the main window
root = tk.Tk()
root.title("Multiplication Table Generator")
root.geometry("400x500")

# Title Label
title_label = ttk.Label(root, text="Multiplication Table Generator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Number Input
ttk.Label(root, text="Enter a number:").pack()
number_entry = ttk.Entry(root)
number_entry.pack(pady=5)

# Range Input
ttk.Label(root, text="Enter range (default 10):").pack()
range_entry = ttk.Entry(root)
range_entry.pack(pady=5)

# Generate Button
generate_button = ttk.Button(root, text="Generate Table", command=generate_table)
generate_button.pack(pady=10)

# Result Display
result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text, font=("Arial", 12), justify="left")
result_label.pack(pady=10)

# Run the application
root.mainloop()
