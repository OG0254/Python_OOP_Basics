class BankAccount(object):
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
    
    def display_info(self):
        print(self.account_holder)
        
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
        print(self.balance)
        
account = BankAccount("Ogada")
account.display_info()
account.deposit(5000)
account.withdraw(6000)
account.display_balance()