class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print("Name: ", self.name, " Age: ", self.age)
        
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        
    def introduce(self):
        print("Name: ", self.name, " Age: ", self.age, " Salary: ", self.salary)
        
details = Person("Ogada", 32)
details.introduce()

details = Employee("Ogada", 32, 100000)
details.introduce()