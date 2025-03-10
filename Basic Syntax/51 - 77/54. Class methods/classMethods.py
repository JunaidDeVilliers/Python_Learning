# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not requre access to the class itself
# Class methods = Best for operations involving the class itself, not instances of the class

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    #INSTANCE METHOD
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"
    
    #CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_average_gpa(cls):
        if cls.count ==0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
#Creating instances
student1 = Student("John", 3.7)
student2 = Student("Jane", 3.8)
student3 = Student("Dave", 3.9)

print(Student.get_count())
print(Student.get_average_gpa())