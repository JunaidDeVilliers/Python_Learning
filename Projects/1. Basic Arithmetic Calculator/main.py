from Calculator import Calculate

if __name__ == '__main__':
    print("Welcome to the Basic Arithmetic Calculator")
    
    valid_operation = False
    
    num1 = ""
    num2 = ""

    while num1.isnumeric() == False:
        num1 = input("Enter your first number: ")
    
    while num2.isnumeric() == False:
        num2 = input("Enter your second number: ")

    num1 = float(num1)
    num2 = float(num2)

    calc = Calculate()

    while valid_operation == False:
        operator = input("Please enter the operation you would like to perform: ")
        match operator:

            case "+":
                print(calc.add(num1, num2))
                valid_operation = True
            case "-":
                print(calc.subtract(num1, num2))
                valid_operation = True
            case "*":
                print(calc.multiply(num1, num2))
                valid_operation = True
            case "/":
                print(calc.divide(num1, num2))
                valid_operation = True
            case _:
                print("Not a valid operation")

# 1. Fix the divide by 0
# 2. Add process to redo until opting out
# 3. Give more details with final print statement
# 4. Optimize and modularize