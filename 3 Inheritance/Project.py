import tkinter as tk
from tkinter import messagebox

# Base Account class
class Account(object):
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        else:
            self.balance -= amount
            return f"Withdrew: {amount}"

    def display_info(self):
        return f"Account holder: {self.account_holder}\nBalance: {self.balance}"

# SavingsAccount subclass
class SavingsAccount(Account):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Interest earned: {interest}"

    def display_info(self):
        return f"Account holder: {self.account_holder}\nBalance: {self.balance}\nInterest Rate: {self.interest_rate}%"

# CurrentAccount subclass
class CurrentAccount(Account):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            return f"Overdraft withdrawal allowed. Withdrew: {amount}"
        else:
            return "Overdraft limit exceeded!"

    def display_info(self):
        return f"Account holder: {self.account_holder}\nBalance: {self.balance}\nOverdraft Limit: {self.overdraft_limit}"

# ---- Tkinter GUI ----
class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Bank App")

        self.account = None  # holds the current account object

        # Entry fields
        tk.Label(root, text="Account Holder Name:").pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()

        tk.Label(root, text="Account Type (account/savings/current):").pack()
        self.type_entry = tk.Entry(root)
        self.type_entry.pack()

        tk.Label(root, text="Interest Rate / Overdraft (if any):").pack()
        self.extra_entry = tk.Entry(root)
        self.extra_entry.pack()

        # Action buttons
        tk.Button(root, text="Create Account", command=self.create_account).pack(pady=5)

        tk.Label(root, text="Amount:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Button(root, text="Deposit", command=self.deposit).pack(pady=2)
        tk.Button(root, text="Withdraw", command=self.withdraw).pack(pady=2)
        tk.Button(root, text="Add Interest (Savings only)", command=self.add_interest).pack(pady=2)
        tk.Button(root, text="Show Account Info", command=self.show_info).pack(pady=5)

    def create_account(self):
        name = self.name_entry.get()
        acc_type = self.type_entry.get().lower()
        extra = self.extra_entry.get()

        if acc_type == "account":
            self.account = Account(name)
            messagebox.showinfo("Success", f"Standard account for {name} created.")
        elif acc_type == "savings":
            if extra:
                self.account = SavingsAccount(name, float(extra))
                messagebox.showinfo("Success", f"Savings account for {name} created.")
            else:
                messagebox.showerror("Error", "Provide interest rate for savings account.")
        elif acc_type == "current":
            if extra:
                self.account = CurrentAccount(name, float(extra))
                messagebox.showinfo("Success", f"Current account for {name} created.")
            else:
                messagebox.showerror("Error", "Provide overdraft limit for current account.")
        else:
            messagebox.showerror("Error", "Invalid account type.")

    def deposit(self):
        if not self.account:
            messagebox.showerror("Error", "Create an account first.")
            return

        try:
            amount = float(self.amount_entry.get())
            message = self.account.deposit(amount)
            messagebox.showinfo("Deposit", message)
        except:
            messagebox.showerror("Error", "Invalid deposit amount.")

    def withdraw(self):
        if not self.account:
            messagebox.showerror("Error", "Create an account first.")
            return

        try:
            amount = float(self.amount_entry.get())
            message = self.account.withdraw(amount)
            messagebox.showinfo("Withdraw", message)
        except:
            messagebox.showerror("Error", "Invalid withdrawal amount.")

    def add_interest(self):
        if not self.account:
            messagebox.showerror("Error", "Create an account first.")
            return

        if isinstance(self.account, SavingsAccount):
            message = self.account.calculate_interest()
            messagebox.showinfo("Interest Added", message)
        else:
            messagebox.showerror("Error", "Only available for Savings Accounts.")

    def show_info(self):
        if not self.account:
            messagebox.showerror("Error", "Create an account first.")
            return

        messagebox.showinfo("Account Info", self.account.display_info())

# Run the app
root = tk.Tk()
app = BankingApp(root)
root.mainloop()
