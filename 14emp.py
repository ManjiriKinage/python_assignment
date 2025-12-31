class Employee:
    total_employees = 0
    male_count = 0
    female_count = 0

    def __init__(self, name, designation, gender, doj, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.doj = doj
        self.salary = salary

        Employee.total_employees += 1

        if gender.lower() == "male":
            Employee.male_count += 1
        elif gender.lower() == "female":
            Employee.female_count += 1

    def salary_above_10000(self):
        return self.salary > 10000

    def is_assistant_manager(self):
        return self.designation.lower() == "assistant manager"


# Creating employee objects
e1 = Employee("Amit", "Manager", "Male", "01-01-2022", 15000)
e2 = Employee("Neha", "Assistant Manager", "Female", "10-03-2021", 12000)
e3 = Employee("Rahul", "Clerk", "Male", "15-07-2023", 8000)
e4 = Employee("Priya", "Assistant Manager", "Female", "20-09-2020", 18000)

employees = [e1, e2, e3, e4]

# a) Total number of employees
print("Total Employees:", Employee.total_employees)

# b) Count of male and female employees
print("Male Employees:", Employee.male_count)
print("Female Employees:", Employee.female_count)

# c) Employees with salary more than 10000
print("\nEmployees with Salary > 10000:")
for emp in employees:
    if emp.salary_above_10000():
        print(emp.name)

# d) Employees with designation Assistant Manager
print("\nAssistant Managers:")
for emp in employees:
    if emp.is_assistant_manager():
        print(emp.name)
