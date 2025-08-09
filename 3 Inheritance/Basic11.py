class Account(object):
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        
    # def display_info(self):
    #     print(self.account_holder)
        
    def deposit(self, amount):
        self.balance += amount
        print("Deposited: ",amount)
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}")

    def display_info(self):
        print(f"Account holder: ", self.account_holder, "Current Balance: ", self.balance)
        
class SavingsAccount(Account):
    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate
        
    def calculate_interest_rate(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest earned: {interest}")
        
    def display_info(self):
        print("Account holder: ", self.account_holder, "Account balance: ", self.balance, "Account interest: ", self.interest_rate)
        
class CurrentAccount(Account):
    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self,amount):
        if self.balance - amount >= -self.overdraft_limit: 
            print("Overdraft withdrawal allowed")
            self.balance -= amount
            print(f"Withdrew: {amount}")

        else:
            print("Overdraft limit exceeded!")
    
    def display_info(self):
        print("Account holder: ", self.account_holder, "Account balance: ", self.balance, "Overdraft: ", self.overdraft_limit)
            
        
Details = Account("Ogada")
Details.deposit(2000)
Details.withdraw(1000)
Details.display_info()

Details2 = SavingsAccount("Ogada", 6.5)
Details2.deposit(2000)
Details2.withdraw(1000)
Details2.calculate_interest_rate()
Details2.display_info()

Details3 = CurrentAccount("Ogada", 4000)
Details3.deposit(4000) #overdraft will be allowed for any amount plus 2000 that you indicated as the overdraft limit
#Details3.withdraw(2000)
Details3.withdraw(9000)
Details3.display_info()