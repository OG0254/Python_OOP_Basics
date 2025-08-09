class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

# Create objects
dog1 = Dog("Spike", 5)
cat1 = Cat("Whiskers", 3)

# Call make_sound()
dog1.make_sound()
cat1.make_sound()
