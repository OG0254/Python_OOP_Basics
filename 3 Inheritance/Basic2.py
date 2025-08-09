class Vehicle(object):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def display_info(self):
        print("Brand: ", self.brand, "Year: ", self.year)
        
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model
        
    def display_info(self):
        #return super().display_info("Brand: ", self.brand, "Year: ", self.year, "Model: ", self.model)
        print("Brand: ,", self.brand, "Year: ,", self.year, "Model: ", self.model)
    
details = Vehicle("Toyota", 2020)
details.display_info()

details = Car("Toyota", 2020, "Premio")
details.display_info()
