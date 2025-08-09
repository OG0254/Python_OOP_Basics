class Laptop(object):
    location = "Kimana"
    
    def __init__(self, brand, price, stock_quantity):
        self.brand = brand
        self.price = price
        self.stock_quantity = stock_quantity
        
    def display_info(self):
        print("Brand: ", self.brand, "Price: ", self.price, "Stock: ", self.stock_quantity)
        
    def update_stock(self, new_stock):
        self.stock_quantity += new_stock
        return self.stock_quantity
        
    @classmethod
    def factory_location(cls):
        return str(cls.location)

class Math:
    @staticmethod
    def convert_usd_to_kes(x):
        return x * 130

details = Laptop("HP", 20000, 10)
details.display_info()

print(f"Factory is located in {Laptop.factory_location()}")

usd_price = 500
kes_price = Math.convert_usd_to_kes(usd_price)
print(f"Price in KES for ${usd_price}: {kes_price}")