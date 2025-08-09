class car(object):
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def my_car(self):
        print("Ogada drives", self.brand, "year of make", self.year)
        
cars = car("Toyota", 2020) 
cars.my_car()
print("Brand: ", cars.brand)
print("Year: ", cars.year)
