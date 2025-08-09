class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def introduce(self):
        print("Hi, I'm", self.name, "and I'm", self.age, "years old.")
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def introduce(self):
        print("Hi, I'm", self.name, "and I'm", self.age, "years old and i teach", self.subject)
        
student = Person("Ogada", 32)
student.introduce()

mwalimu = Teacher("Brian", 35, "Python")
mwalimu.introduce()