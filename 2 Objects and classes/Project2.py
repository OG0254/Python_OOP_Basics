import tkinter as tk
from tkinter import messagebox, simpledialog

# --- Laptop Class ---
class Laptop:
    def __init__(self, brand, model, price, stock_quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock_quantity = stock_quantity

    def sell(self, quantity):
        if quantity > self.stock_quantity:
            return f"Only {self.stock_quantity} left for {self.model}!"
        else:
            self.stock_quantity -= quantity
            return f"{self.model}: Successfully sold {quantity} laptop(s)."

    def restock(self, quantity):
        self.stock_quantity += quantity
        return f"{self.model}: Successfully restocked {quantity} laptop(s)."

    def get_details(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nPrice: KES {self.price}\nStock: {self.stock_quantity}"

# --- Inventory ---
inventory = {
    "hp": [
        Laptop("HP", "840", 100000, 10),
        Laptop("HP", "830", 100000, 20)
    ],
    "dell": [
        Laptop("Dell", "XPS", 120000, 7)
    ],
    "lenovo": [
        Laptop("Lenovo", "ThinkPad", 95000, 12)
    ],
    "asus": [
        Laptop("Asus", "ZenBook", 110000, 5)
    ]
}

# --- Functions ---
def search_laptop():
    key = entry_search.get().lower()
    if key in inventory:
        result = ""
        for laptop in inventory[key]:
            result += laptop.get_details() + "\n\n"
        messagebox.showinfo("Laptops Found", result)
    else:
        messagebox.showerror("Not Found", "Laptop brand not found in inventory.")

def select_model(brand):
    models = [laptop.model for laptop in inventory[brand]]
    selected_model = simpledialog.askstring("Select Model", f"Available models: {', '.join(models)}\nType model to proceed:")
    if selected_model:
        for laptop in inventory[brand]:
            if laptop.model.lower() == selected_model.lower():
                return laptop
        messagebox.showerror("Error", "Model not found.")
    return None

def sell_laptop():
    key = entry_search.get().lower()
    if key in inventory:
        try:
            qty = int(entry_quantity.get())
            selected_laptop = select_model(key)
            if selected_laptop:
                result = selected_laptop.sell(qty)
                messagebox.showinfo("Sell Operation", result)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid quantity.")
    else:
        messagebox.showerror("Not Found", "Laptop brand not found.")

def restock_laptop():
    key = entry_search.get().lower()
    if key in inventory:
        try:
            qty = int(entry_quantity.get())
            selected_laptop = select_model(key)
            if selected_laptop:
                result = selected_laptop.restock(qty)
                messagebox.showinfo("Restock Operation", result)
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid quantity.")
    else:
        messagebox.showerror("Not Found", "Laptop brand not found.")

def show_all_stock():
    result = ""
    for key in inventory:
        for laptop in inventory[key]:
            result += f"{laptop.brand} {laptop.model} - {laptop.stock_quantity} in stock\n"
    messagebox.showinfo("Current Stock", result)

# --- Tkinter GUI Setup ---
root = tk.Tk()
root.title("Laptop Inventory System")
root.geometry("450x500")
root.resizable(False, False)

title_label = tk.Label(root, text="Laptop Inventory System", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

search_label = tk.Label(root, text="Laptop Brand (e.g. 'HP'):")
search_label.pack(pady=5)

entry_search = tk.Entry(root, width=30, justify="center")
entry_search.pack(pady=5)

qty_label = tk.Label(root, text="Quantity:")
qty_label.pack(pady=5)

entry_quantity = tk.Entry(root, width=10, justify="center")
entry_quantity.pack(pady=5)

# Buttons
search_button = tk.Button(root, text="Search Laptop", command=search_laptop, width=25)
search_button.pack(pady=5)

sell_button = tk.Button(root, text="Sell Laptop(s)", command=sell_laptop, bg="green", fg="white", width=25)
sell_button.pack(pady=5)

restock_button = tk.Button(root, text="Restock Laptop(s)", command=restock_laptop, bg="orange", fg="white", width=25)
restock_button.pack(pady=5)

stock_button = tk.Button(root, text="Show All Stock", command=show_all_stock, width=25)
stock_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.quit, bg="red", fg="white", width=25)
exit_button.pack(pady=5)

root.mainloop()
