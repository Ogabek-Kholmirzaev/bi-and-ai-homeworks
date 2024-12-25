import os

class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
    def __repr__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}"
    
    def to_csv(self):
        return f"{self.employee_id},{self.name},{self.position},{self.salary}\n"

    @staticmethod
    def from_csv(line):
        parts = line.strip().split(",")
        return Employee(parts[0], parts[1], parts[2], parts[3])

class EmployeeManager:
    FILE_NAME = "employees.txt"
    
    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as file:
                pass
    
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")

        with open(self.FILE_NAME, "a") as file:
            file.write(Employee(emp_id, name, position, salary).to_csv())
        
        print("Employee added successfully!")
    
    def view_all_employees(self):
        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No employees found.")
            return
        
        for line in lines:
            print(Employee.from_csv(line))
    
    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")

        with open(self.FILE_NAME, "r") as file:
            for line in file:
                employee = Employee.from_csv(line)

                if employee.employee_id == emp_id:
                    print("Employee Found:", employee)
                    return
                
        print("Employee not found.")
    
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        updated = False

        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for line in lines:
                employee = Employee.from_csv(line)

                if employee.employee_id == emp_id:
                    name = input("Enter new Name: ")
                    position = input("Enter new Position: ")
                    salary = input("Enter new Salary: ")

                    file.write(Employee(emp_id, name, position, salary).to_csv())
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Employee updated successfully!")
        else:
            print("Employee not found.")
    
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        deleted = False

        with open(self.FILE_NAME, "r") as file:
            lines = file.readlines()

        with open(self.FILE_NAME, "w") as file:
            for line in lines:
                employee = Employee.from_csv(line)
                if employee.employee_id == emp_id:
                    deleted = True
                else:
                    file.write(line)

        if deleted:
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    def menu(self):
        while True:
            print("\nEmployee Records Manager")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.view_all_employees()
            elif choice == "3":
                self.search_employee()
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete_employee()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

manager = EmployeeManager()
manager.menu()