class Student(object):
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.grades = [ ] 
        #self.count = 0
        
    def display_info(self):
        print(self.name, self.age, self.course)
        
    def add_grade(self, grades):
        self.grades.append(grades)
        print(grades)
    
    def display_grades(self):
        print(self.grades)
        
    def get_average(self):
        return sum(self.grades) / len(self.grades)  # once you use RETURN use print for results to be seen on the screen
    #OR
        #average = sum(self.grades) / len(self.grades) 
        #return self.count / self.count
    
    def check_pass(self):
        average = sum(self.grades) / len(self.grades)
        if average >= 60:
            print("Passed")
        else:
            print("Failed")

student1 = Student("Brian", 32, "Python 101")

student1.display_info()
student1.add_grade(80)
student1.add_grade(90)
student1.add_grade(75)

student1.display_grades()

print(student1.get_average())

student1.check_pass()