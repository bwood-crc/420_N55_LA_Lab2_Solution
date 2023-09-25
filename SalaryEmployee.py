import decimal
from Employee import *


class SalaryEmployee(Employee):

    def __init__(self, id, name, pay_method, yearly_salary):
        super().__init__(id, name, pay_method)
        self.yearly_salary = yearly_salary

    def calculate_salary(self, amount=Decimal(0)):
        return super().calculate_salary(self.yearly_salary / 12)
