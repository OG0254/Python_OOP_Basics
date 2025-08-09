class Vehicle(object):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print("Brand: ", self.brand, "Year: ", self.year)
        
class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_capacity):
        super().__init__(brand, year)
        self.engine_capacity = engine_capacity
        
    def display_info(self):
        print("Brand: ", self.brand, "Year: ", self.year, "Engine capacity: ", self.engine_capacity)
        
vehicle1 = Vehicle("Toyota", 2020)
vehicle1.display_info()

bike1 = Motorcycle("Yamaha", 2023, "250cc")
bike1.display_info()