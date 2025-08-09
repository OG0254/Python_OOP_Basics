class Appliance(object):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def display_info(self):
        print("Brand: ", self.brand, "| Price: ", self.price)
        
class Fridge(Appliance):
    def __init__(self, brand, price, capacity):
        super().__init__(brand, price)
        self.capacity = capacity
        
    def display_info(self):
        print("Brand: ", self.brand, "| Price: ", self.price, "| Capacity: ", self.capacity)
        
details = Appliance("LG", 200000)
details.display_info()

details = Fridge("Samsung", 300000, "150 Litres")
details.display_info()