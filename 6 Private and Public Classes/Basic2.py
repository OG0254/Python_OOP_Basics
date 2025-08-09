class Bank:
    class __Account:
        def __init__(self, account_holder, balance):
            self.account_holder = account_holder
            self.balance = balance

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
            return f"Account holder: {self.account_holder} | Balance: {self.balance}"

    def __init__(self, account_holder, balance):
        self.__account = self.__Account(account_holder, balance)

    def deposit(self, amount):
        return self.__account.deposit(amount)

    def withdraw(self, amount):
        return self.__account.withdraw(amount)

    def display_info(self):
        return self.__account.display_info()


# Usage
my_account = Bank("Ogada", 5000)

print(my_account.deposit(2000))     # Deposited: 2000
print(my_account.withdraw(1000))    # Withdrew: 1000
print(my_account.display_info())    # Account holder: Ogada | Balance: 6000
