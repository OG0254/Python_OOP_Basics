class Appliances(object):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        
    def display_info(self):
        print("Brand: ", self.brand, "Price: ", self.price,)
        
    def update_price(self, new_price):
        self.price = new_price
        
    def display_price_update(self):
        print("After price update:")
        
class WashingMachine(Appliances):
    def __init__(self, brand, price, capacity):
        super().__init__(brand, price)
        self.capacity = capacity
            
    def display_info(self):
        print("Brand: ", self.brand, "Price: ", self.price, "Capacity: ", self.capacity)
        
    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        
    def display_capacity_update(self):
        print("After capacity update:")
        
details1 = Appliances("Samsung", 50000)
details1.display_info()

details2 = WashingMachine("LG", 70000, "8KG")
details2.display_info()
details2.display_price_update()

details2 = WashingMachine("LG", 75000, "8KG")
details2.display_info()
details2.display_capacity_update()

details2 = WashingMachine("LG", 70000, "10KG")
details2.display_info()