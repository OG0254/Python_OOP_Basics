print("Welcome Brian!")

class BankAccount:
    def __init__(self):
        self.balance = 0  # Every account starts with 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")

# Create one account instance
account = BankAccount()

# Perform operations
account.deposit(2000)
account.withdraw(1000)
account.display_balance()
