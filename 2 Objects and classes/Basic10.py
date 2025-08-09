import sys

class Laptop(object):
    def __init__(self, brand, model, price, stock_quantity):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock_quantity = stock_quantity
        
    def display_details(self):
        print(self.brand, self.model, self.price, self.stock_quantity)
        
    def update_price(self, new_price):
        self.price += new_price
        
    def update_stock(self, new_stock):
        self.stock_quantity += new_stock
        
    def sell(self):
        while True:
            quantity = int(input("Enter quantity to sell: "))
            if quantity > self.stock_quantity:
                print("Insufficient quantity!")
                choice = input("Do you want to try again? (yes/no): ").lower()
                if choice == 'no':
                    print("Exiting transaction.")
                    sys.exit()  # <- THIS should be inside the 'if' block
                elif choice == 'yes':
                    continue  # ask for quantity again
                else:
                    print("Invalid input. Exiting transaction.")
                    sys.exit()
            else:
                self.stock_quantity -= quantity
                print(f"Sold: {quantity}")
                break  # sale done, exit loop

    def restock(self, quantity):
        self.stock_quantity += quantity

# --- program flow ---

specs = Laptop("HP", 840, 100000, 10)
specs.display_details()

specs.update_price(10000)
specs.update_stock(5)
specs.display_details()

specs.sell()  # interactive sale
specs.display_details()

specs.restock(5)
specs.display_details()
