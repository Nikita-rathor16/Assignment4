"""import faker"""
from faker import Faker
class Employee:
    """create class employee"""
    def __init__(self):
        self._employee_id = None
        self._name = None
        self._email = None
        self._business_unit = None
        self._salary = None
        self.fake = Faker()
    @property
    def employee_id(self):
        """return employee_id"""
        return self._employee_id
    @employee_id.setter
    def employee_id(self, value):
        self._employee_id = value
    @property
    def name(self):
        """return name"""
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def email(self):
        """return email"""
        return self._email
    @email.setter
    def email(self, value):
        self._email = value
    @property
    def business_unit(self):
        """return business unit"""
        return self._business_unit
    @business_unit.setter
    def business_unit(self, value):
        self._business_unit = value
    @property
    def salary(self):
        """return salary"""
        return self._salary
    @salary.setter
    def salary(self, value):
        self._salary = value
    def set_default_values(self):
        """this is set default value method"""
        self._employee_id = self.fake.unique.random_number(digits=5)
        self._name = self.fake.name()
        self._email = self.fake.email()
        self._business_unit = self.fake.company()
        self._salary = self.fake.random_int(min=30000, max=120000)
# Example usage
employee = Employee()
employee.set_default_values()
print(f"Employee ID: {employee.employee_id}, Name: {employee.name}",
      f"Email: {employee.email}, Business Unit: {employee.business_unit}",
      f"Salary: {employee.salary}")
