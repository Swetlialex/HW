class Employee:
    """Represents an employee with a name, ID, salary, and department."""

    def __init__(self, name, emp_id, salary, department):
        """Initializes an Employee object with the given attributes."""
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    
# Create 5 employee objects with different salaries
employees = [
    Employee("Ivan Petrov", 1234567890, 50000, "Engineering"),
    Employee("Maria Ivanova", 9876543210, 65000, "Marketing"),
    Employee("Mihail Georgiev", 2345678901, 48000, "Sales"),
    Employee("Alisa Stoyanova", 3456789012, 52000, "Human Resources"),
    Employee("Bogomil Nikolov", 5678901234, 70000, "Finance"),
]
def get_salary(employees):
        return employees.salary

# Сортираме служителите по заплата в низходящ ред
# top_earners = sorted(employees, key=lambda emp: emp.salary, reverse=True)[:3]
top_earners = sorted(employees, key=get_salary, reverse=True)[:3]

# Отпечатваме информацията за тримата най-високоплатени служители
i = 1 # помощна променлива за отпечатване на първия, втория и третия служител
print("Top 3 Employee with the highest salary:")
for emp in top_earners:
    print(f"\n#{i}")
    print(f"Name: {emp.name}")
    print(f"ID: {emp.emp_id}")
    print(f"Salary: ${emp.salary}")
    print(f"Department: {emp.department}")
    i+=1




### EXPECTED OUTPUT:
# #1
# Name: Bogomil Nikolov
# ID: 5678901234
# Salary: $70000
# Department: Finance

# #2
# Name: Maria Ivanova
# ID: 9876543210
# Salary: $65000
# Department: Marketing

# #3
# Name: Alisa Stoyanova
# ID: 3456789012
# Salary: $52000
# Department: Human Resources