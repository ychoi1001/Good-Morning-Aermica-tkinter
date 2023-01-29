import tkinter as tk
from tkinter import messagebox

# Set price using dictionary
menu = {'Egg': 0.99, 'Bacon': 0.49, 'Sausage': 1.49, 'Hash Brown': 1.19, 'Toast': 0.79, 'Coffee': 1.09, 'Small Breakfast': 6.23, 'Regular Breakfast': 9.69, 'Big Breakfast': 15.92}

# To save items when placing order
items = {}

# Set sum = 0 to calculate the cost in total
totalPrice = 0

# Add items
def add(item):
    # Create a global variable
    global totalPrice

    # Check if user select a correct item
    if item not in menu:
        print("Not exists in our menu")
    
    # Get price of item
    itemPrice = menu.get(item)

    # Calculate total price
    totalPrice += itemPrice

    # Count the number of items in my basket
    if item in items:
        items[item] = items.get(item) + 1
    else:
        items[item] = 1
    
    # Print/update order in the basket and print/update price
    print_order()
    print_price()

# To print order in basket
def print_order():
    # Set global variable items
    global items
    tmp = ""

    # To show all the orders
    for i in items:
        tmp = tmp + i + " X " + str(items.get(i)) + "\n"
    
    # Delete texts before update
    basket.delete('1.0', tk.END)

    # Insert updated order
    basket.insert(tk.INSERT, tmp)

# To print total price
def print_price():
    # Set global variable
    global totalPrice

    # Print final price
    labelPrice.configure(text="$"+str(round(totalPrice,2)))

# Place order
def place_order(): 
    # Reset all
    global totalPrice, items
    totalPrice = 0
    del items # Delete items

    items = {}
    print_price()
    print_order()    
    

# Window = instance of Tkinter's Tk class
# Create a new window and assign it to the variable window
window = tk.Tk()

# Set title of window
window.title('Good Morning, America!')

# Set width and height
window.geometry("600x550")

# Not resizable
window.resizable(False, False)

# Use Frame to group and organize other widgets
# frame1 for buttons
frame1 = tk.Frame(window)
frame1.pack()

# frame2 for a basket
frame2 = tk.Frame(window)
frame2.pack()

# frame3 for a total price
frame3 = tk.Frame(window)
frame3.pack(side="bottom", fill="x")

# Place buttons
# Get list of menu
listOfMenu = list(menu.keys())

# Get number of menu
numMenu = len(listOfMenu)

# Set count = 0
countMenu = 0

# Generate buttons in frame1
tk.Button(frame1, text="Egg", command=lambda : add('Egg'), width=10, height=2).grid(row=0, column=0)
tk.Button(frame1, text="Bacon", command=lambda : add('Bacon'), width=10, height=2).grid(row=0, column=1)
tk.Button(frame1, text="Sausage", command=lambda : add('Sausage'), width=10, height=2).grid(row=0, column=2)
tk.Button(frame1, text="Hash Brown", command=lambda : add('Hash Brown'), width=10, height=2).grid(row=1, column=0)
tk.Button(frame1, text="Toast", command=lambda : add('Toast'), width=10, height=2).grid(row=1, column=1)
tk.Button(frame1, text="Coffee", command=lambda : add('Coffee'), width=10, height=2).grid(row=1, column=2)
tk.Button(frame1, text="Small Breakfast", command=lambda : add('Small Breakfast'), width=10, height=2).grid(row=2, column=0)
tk.Button(frame1, text="Regular Breakfast", command=lambda : add('Regular Breakfast'), width=10, height=2).grid(row=2, column=1)
tk.Button(frame1, text="Big Breakfast", command=lambda : add('Big Breakfast'), width=10, height=2).grid(row=2, column=2)

# Create a basket in frame2
basket = tk.Text(frame2)
basket.pack()

# Create a Order button in frame3
tk.Button(frame3, text="Place order", command=place_order, width=10, height=2, padx=5, pady=5).grid(row=0, column=0)

# Place text for total in frame3
labelPrice = tk.Label(frame3, text="Total: 0", width=80, padx=10, pady=10, font=("Arial", 15))
labelPrice.grid(row=0, column=2)

# Run Tkinter event loop
window.mainloop()