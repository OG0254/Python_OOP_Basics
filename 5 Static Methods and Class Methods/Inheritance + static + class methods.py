class Product:
    warranty_years = 2  # class attribute shared by all products
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product: {self.name}, Price: {self.price} KES")

    @classmethod
    def get_warranty(cls):
        return f"Warranty: {cls.warranty_years} years"

    @staticmethod
    def convert_usd_to_kes(usd):
        return usd * 130


class Laptop(Product):
    def __init__(self, name, price, ram):
        super().__init__(name, price)
        self.ram = ram

    def display_info(self):
        print(f"Laptop: {self.name}, Price: {self.price} USD, RAM: {self.ram}")


# Example Usage
laptop1 = Laptop("HP Elitebook", 800, "16GB")
laptop1.display_info()

# Inherited class method
print(Laptop.get_warranty())

# Static method use
price_in_kes = Product.convert_usd_to_kes(800)
print(f"Price in KES: {price_in_kes}")
