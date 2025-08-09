class Student(object):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        
    def introduce(self):
        print("Hi, my name is", self.name , "I am", self.age, "years old and I'm studying", self.course)
        
    def change_data(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        

details = Student("Brian", 24, "Computer Science.")        
details.introduce()
details.change_data("Ogada", 32, "ICT.")
details.introduce()
details.change_data("Kim", 40, "HR.")
details.introduce()
