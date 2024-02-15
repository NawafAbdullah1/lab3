employees = {}

while True:
    name = input("Enter the name of the employee ('no' to exit): ")
    if name.lower() == 'no':
        break
    salary = int(input("Enter the salary of {}: ".format(name)))
    employees[name] = salary

print("the employees dictionary:", employees)

