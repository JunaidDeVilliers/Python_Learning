# class variables = Shared aming all instances of a class
#                   Defined in the constructor
#                   Allows you to share among all objects created from that class

class Student:

    class_year = "2021" # class variable
    num_students = 0 # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # Adds 1 student every time a new student is created

Student1 = Student("Alice", 20)
Student2 = Student("Bob", 21)
Student3 = Student("Charlie", 22)
Student4 = Student("David", 23)

print(f"My graduating class of {Student.class_year} has {Student.num_students} students.")
# it is good practice to access class variables using the class name instead of the instance name

print(Student1.name)
print(Student2.name)
print(Student3.name)
print(Student4.name)