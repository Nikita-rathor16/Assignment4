"""import json"""
import json
class Employee:
    """create employee class"""
    def __init__(self, employee_id, name, email, business_unit, salary):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.business_unit = business_unit
        self.salary = salary
    def to_dict(self):
        """return id,name,email,unit,salary"""
        return {
            "EMP ID": self.employee_id,
            "EMP NAME": self.name,
            "EMP EMAIL": self.email,
            "Business Unit": self.business_unit,
            "Salary": self.salary
        }
    @staticmethod
    def to_json_and_write(employees=None, file_name="employees.json"):
        """define function and write to json"""
        if employees is None:
            employees = []
        # Convert to JSON
        if isinstance(employees, list):
            data = [emp.to_dict() for emp in employees]
        else:
            data = employees.to_dict()
        # Write to file
        with open(file_name, "w",encoding="utf-8") as file:
            json.dump(data, file, indent=4)
# Example usage
employee1 = Employee(1, "nikki", "nikki@gmail.com", "Engineering", 75000)
employee2 = Employee(2, "Nikita", "Nikita@example.com", "Marketing", 80000)
employee3 = Employee(3, "Alice", "alice@example.com", "HR", 60000)
employee1.to_json_and_write(file_name="employee1.json")
employees_list = [employee1, employee2, employee3]
Employee.to_json_and_write(employees_list, "employees_list.json")
Employee.to_json_and_write()
