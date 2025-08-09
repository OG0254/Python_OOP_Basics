class Product:
    warranty_years = 2  # class attribute shared by all products
    currency_rate = 130
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price} KES")

    @classmethod
    def get_warranty(cls):
        return f"Warranty: {cls.warranty_years} years"
    
    @classmethod
    def get_currency_rate(cls):
        return f"Currency rate: {cls.currency_rate} KES"

    @staticmethod
    def convert_usd_to_kes(usd):
        return usd * 130


class Laptop(Product):
    def __init__(self, name, price, ram):
        super().__init__(name, price)
        self.ram = ram

    def display_info(self):
        print(f"Laptop: {self.name}, Price: {self.price} USD, RAM: {self.ram}")
        
    def display_prices(self):
        print(f"Price in USD: {self.price}")


# Example Usage
laptop1 = Laptop("HP Elitebook", 800, "16GB")
laptop1.display_info()

# Inherited class method
print(Laptop.get_warranty())
print(Laptop.get_currency_rate())

laptop1.display_prices()
# Static method use
price_in_kes = Product.convert_usd_to_kes(800)
print(f"Price in KES: {price_in_kes}")
