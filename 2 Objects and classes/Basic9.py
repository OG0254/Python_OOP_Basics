class Employee(object):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    def display_info(self):
        print("Name: ", self.name, "| Position: ", self.position, "| Salary: ", self.salary)
        
    def give_raise(self, amount):
        self.salary += amount
        
    def change_position(self, new_position):
        self.position = new_position
        
payroll1 = Employee("Ogada", "ICT Lead", 90000)
payroll1.display_info()
payroll2 = Employee("Brian", "ICT Support", 70000)
payroll2.display_info()
payroll1.give_raise(140000)
payroll1.change_position("ICT Manager")
payroll1.display_info()
payroll2.display_info()