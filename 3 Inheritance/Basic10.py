class Account(object):
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")

    def display_info(self):
        print(f"Account holder: {self.account_holder}, Current Balance: {self.balance}")

class FixedDepositAccount(Account):
    def __init__(self, account_holder, balance, maturity_period):
        super().__init__(account_holder, balance)
        self.maturity_period = maturity_period  # in months

    def withdraw(self, amount, months_passed):
        if months_passed < self.maturity_period:
            print(f"Withdrawal not allowed before maturity of {self.maturity_period} months. You’re at {months_passed} months.")
        else:
            super().withdraw(amount)

    def display_maturity_status(self, months_passed):
        remaining = self.maturity_period - months_passed
        if remaining > 0:
            print(f"{remaining} months until maturity.")
        else:
            print("Account has matured. Withdrawals are allowed.")

# Example Usage
acc1 = Account("Ogada", 5000)
acc1.deposit(1000)
acc1.withdraw(2000)
acc1.display_info()

print("\n--- Fixed Deposit Account ---")

acc2 = FixedDepositAccount("Brian", 10000, 12)
acc2.display_maturity_status(12)
acc2.withdraw(500, 12)# Blocked
acc2.display_info()


