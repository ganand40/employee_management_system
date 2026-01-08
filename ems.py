#Initializing data store
employees = {
    101: {
        'name' : 'john',
        'age' : 30,
        'department' : 'hr',
        'salary' : 40000
    },
    102: {
        'name' : 'alex',
        'age' : 25,
        'department' : 'sales',
        'salary' : 23000
    },
    103: {
        'name' : 'mike',
        'age' : 40,
        'department' : 'sales',
        'salary' : 60000
    }
}

#Define Menu System
# Create a menu that displays the following options:
# Add Employee
# View All Employees
# Search for Employee
# Update the Employee
# Delete the Employee
# Exit

def main_menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

def add_employee():
    emp_id = int(input("Enter Employee ID: "))

    if emp_id in employees:
        print("Employee ID already exists. Please use a unique ID.")
        return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("Employee added successfully.")

def view_employees():
    if not employees:
        print("No employees available.")
        return

    print("\nID\tName\tAge\tDepartment\tSalary")
    print("-" * 90)

    for emp_id, details in employees.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t\t{details['salary']}")

def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Found:")
        print("Name:", emp['name'])
        print("Age:", emp['age'])
        print("Department:", emp['department'])
        print("Salary:", emp['salary'])
    else:
        print("Employee not found.")

def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))

    if emp_id not in employees:
        print("Employee not found.")
        return

    print("\nLeave field empty to keep current value.")

    name = input(f"Enter Name ({employees[emp_id]['name']}): ")
    age = input(f"Enter Age ({employees[emp_id]['age']}): ")
    department = input(f"Enter Department ({employees[emp_id]['department']}): ")
    salary = input(f"Enter Salary ({employees[emp_id]['salary']}): ")

    if name:
        employees[emp_id]['name'] = name
    if age:
        employees[emp_id]['age'] = int(age)
    if department:
        employees[emp_id]['department'] = department
    if salary:
        employees[emp_id]['salary'] = int(salary)

    print("Employee record updated successfully.")

def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    if emp_id in employees:
        del employees[emp_id]
        print("Employee record deleted successfully.")
    else:
        print("Employee not found.")


# Program execution starts here
main_menu()

