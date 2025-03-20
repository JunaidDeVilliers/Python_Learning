employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]


file_path = "employees.txt"

try:
    with open(file_path, "w") as file:
        for employee in employees: 
            file.write(employee + "\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")