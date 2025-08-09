class Student(object):
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.grades = [ ]
    
    def display_info(self):
        print(self.name, self.course)
            
    def add_grade(self, grades):
        self.grades.append(grades)
        print(grades)
        
    def display_grades(self):
        print(self.grades)
        
    def average_grade(self):
        return sum(self.grades) / len(self.grades)
    
student1 = Student("Brian", "Python 101")

student1.display_info()
student1.add_grade(80)
student1.add_grade(90)
student1.add_grade(75)

student1.display_grades()

print(student1.average_grade())