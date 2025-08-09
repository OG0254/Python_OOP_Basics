class Account(object):
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self._balance = 0
        self._pin = 1234  # Default pin

    def set_private_info(self, balance, pin):
        self._balance = balance
        self._pin = pin

    def deposit(self, amount):
        self._balance += amount
        return f"Deposited: {amount}"

    def withdraw(self, pin, amount):
        if pin != self._pin:
            return "Incorrect pin!"
        elif amount > self._balance:
            return "Insufficient funds!"
        else:
            self._balance -= amount
            return f"Withdrew: {amount}"
        
    def display_info(self):
        return f"Account holder: {self.account_holder}\nBalance: {self._balance}"

# Usage
details = Account("Ogada")
details.set_private_info(1000, 1234)  # Set initial balance and pin
print(details.deposit(2000))
print(details.withdraw(1111, 500))  # Correct pin
print(details.display_info())