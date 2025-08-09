import tkinter as tk
from tkinter import messagebox

# Define Laptop class
class Laptop:
    def __init__(self, brand, model, price, stock_quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock_quantity = stock_quantity

    def sell(self, quantity):
        if quantity > self.stock_quantity:
            return "Insufficient stock available!"
        else:
            self.stock_quantity -= quantity
            return f"Successfully sold {quantity} laptop(s)."

    def restock(self, quantity):
        self.stock_quantity += quantity
        return f"Successfully restocked {quantity} laptop(s)."

    def get_stock(self):
        return f"{self.stock_quantity} laptop(s) in stock."

# Create Laptop object
laptop = Laptop("HP", "EliteBook 840", 100000, 10)

# Tkinter window setup
root = tk.Tk()
root.title("Laptop Inventory Management")
root.geometry("420x350")
root.resizable(False, False)

# --- Functions for buttons ---

def show_details():
    details = (
        f"Brand: {laptop.brand}\n"
        f"Model: {laptop.model}\n"
        f"Price: KES {laptop.price}\n"
        f"Stock: {laptop.stock_quantity}"
    )
    messagebox.showinfo("Laptop Details", details)

def sell_item():
    try:
        qty = int(entry_quantity.get())
        if qty <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            return
        result = laptop.sell(qty)
        messagebox.showinfo("Sale", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number.")

def restock_item():
    try:
        qty = int(entry_quantity.get())
        if qty <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive number.")
            return
        result = laptop.restock(qty)
        messagebox.showinfo("Restock", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter a valid number.")

def check_stock():
    result = laptop.get_stock()
    messagebox.showinfo("Current Stock", result)

# --- Widgets ---

title_label = tk.Label(root, text="Laptop Inventory System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

details_button = tk.Button(root, text="Show Laptop Details", command=show_details, width=25)
details_button.pack(pady=5)

qty_label = tk.Label(root, text="Quantity:")
qty_label.pack(pady=5)

entry_quantity = tk.Entry(root, width=10, justify="center")
entry_quantity.pack(pady=5)

sell_button = tk.Button(root, text="Sell Laptop(s)", command=sell_item, bg="green", fg="white", width=20)
sell_button.pack(pady=5)

restock_button = tk.Button(root, text="Restock Laptop(s)", command=restock_item, bg="orange", fg="white", width=20)
restock_button.pack(pady=5)

stock_button = tk.Button(root, text="Check Current Stock", command=check_stock, width=25)
stock_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=20)
exit_button.pack(pady=5)

# Run the window
root.mainloop()
