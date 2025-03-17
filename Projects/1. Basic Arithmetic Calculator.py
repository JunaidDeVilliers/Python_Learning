if __name__ == '__main__':
    print("Welcome to the Basic Arithmetic Calculator")
    
    valid_operation = False

    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    def add(num1, num2, operator):
        print(f"{num1} {operator} {num2} = {num1 + num2}")

    def subtract(num1, num2, operator):
        print(f"{num1} {operator} {num2} = {num1 - num2}")

    def divide(num1, num2, operator):
        print(f"{num1} {operator} {num2} = {num1 / num2}")

    def multiply(num1, num2, operator):
        print(f"{num1} {operator} {num2} = {num1 * num2}")

    while valid_operation == False:
        operator = input("Please enter the operation you would like to perform: ")

        match operator:
            case "+":
                add(num1, num2, operator)
                valid_operation = True
            case "-":
                subtract(num1, num2, operator)
                valid_operation = True
            case "*":
                multiply(num1, num2, operator)
                valid_operation = True
            case "/":
                divide(num1, num2, operator)
                valid_operation = True
            case _:
                print("Not a valid operation")

