# Static method = A method that belongs to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods   = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_postions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_postions
    
employee1 = Employee("John", "Manager")
employee2 = Employee("Cindy", "Cashier")
employee3 = Employee("Alice", "Cook")

print(Employee.is_valid_position("Manager")) # True
print(employee1.is_valid_position("Manager")) # True
print(employee2.is_valid_position("Manager")) # True
print(employee3.is_valid_position("Manager")) # True