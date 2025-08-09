class Product(object):
    def __init__(self, name, category, price, stock_quantity):
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
        
    def display_product(self):
        print(self.name, self.category, self.price, self.stock_quantity)
        
    def changes(self, new_price, new_stock):
        self.price = new_price
        self.stock_quantity = new_stock
    # def update_stock(self, new_stock):
    #     self.stock_quantity = new_stock
        
product1 = Product("Oil", "Cooking", 200, 5)
product1.display_product()
product2 = Product("Milk", "Breakfast", 50, 10)
product2.display_product()
product1.changes(250, 8)
product1.display_product()
product2.display_product()