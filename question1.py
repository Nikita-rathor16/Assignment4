"""import faker"""
import json
import random
from faker import Faker
class Employee:
    """create class to employee"""
    def __init__(self, employee_id, name, email, business_unit, salary):
        """create function to employee id .. etc"""
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.business_unit = business_unit
        self.salary = salary
fake = Faker()
# Generate fake employee data
employee_records = []
for _ in range(random.randint(50, 100)):
    employee_id = fake.unique.random_number(digits=5)
    name = fake.name()
    email = fake.email()
    business_unit = fake.company()
    salary = fake.random_int(min=30000, max=120000)
    employee_records.append({
        "EMP ID": employee_id,
        "EMP NAME": name,
        "EMP EMAIL": email,
        "Business Unit": business_unit,
        "Salary": salary
    })
# Save data to JSON file
with open("Employee_Personal_Details.json", "w", encoding="utf-8") as file:
    json.dump(employee_records, file, indent=4)
# Load data into Employee objects
employees = []
for record in employee_records:
    employee = Employee(record["EMP ID"],
                        record["EMP NAME"], record["EMP EMAIL"],
                          record["Business Unit"], record["Salary"])
    employees.append(employee)
# Example usage
for emp in employees:
    print(f"Employee ID: {emp.employee_id}, Name: {emp.name}",
          f"Email: {emp.email}, Business Unit: {emp. business_unit}",
          f"Salary: {emp.salary}")
