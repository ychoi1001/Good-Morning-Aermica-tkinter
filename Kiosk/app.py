import tkinter as tk
from tkinter import messagebox

# Set price using dictionary
price = {'Egg': 0.99, 'Bacon': 0.49, 'Sausage': 1.49, 'Hash Brown': 1.19, 'Toast': 0.79, 'Coffee': 1.09, 'Small Breakfast': 6.23, 'Regular Breakfast': 9.69, 'Big Breakfast': 15.92}

# Set sum = 0 to calculate the cost in total
sum = 0

# Window = instance of Tkinter's Tk class
# Create a new window and assign it to the variable window
window = tk.Tk()

# Set title of window
window.title('Menu')

# Set width and height
window.geometry("600x900")

# Use Frame to group and organize other widgets
frame = tk.Frame(window)
frame.pack()

# Place buttons
tk.Button(frame, text="Egg", width=10, height=2).grid(row=0, column=0)
tk.Button(frame, text="Bacon", width=10, height=2).grid(row=0, column=1)
tk.Button(frame, text="Sausage", width=10, height=2).grid(row=0, column=2)
tk.Button(frame, text="Hash Brown", width=10, height=2).grid(row=1, column=0)
tk.Button(frame, text="Toast", width=10, height=2).grid(row=1, column=1)
tk.Button(frame, text="Coffee", width=10, height=2).grid(row=1, column=2)
tk.Button(frame, text="Small Breakfast", width=10, height=2).grid(row=2, column=0)
tk.Button(frame, text="Regular Breakfast", width=10, height=2).grid(row=2, column=1)
tk.Button(frame, text="Big Breakfast", width=10, height=2).grid(row=2, column=2)

# Place text for total
label = tk.Label(window, text="Total: 0", width=100, height=5, font=("Helvetica", 18))
label.place(relx=0.0, rely=1.0, anchor='sw')


window.mainloop()