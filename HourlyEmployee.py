from decimal import Decimal
from Employee import *
from PayMethod import *


class HourlyEmployee(Employee):

    def __init__(self, id, name: str, pay_method: PayMethod, yearly_salary: Decimal):
        super().__init__(id, name, pay_method)
        self.hourly_rate = yearly_salary

    def calculate_salary(self, amount=Decimal(0)):
        return super().calculate_salary(self.hourly_rate * 160)
