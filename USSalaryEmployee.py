from SalaryEmployee import *
from USEmployeeInterface import *


class USSalaryEmployee(SalaryEmployee, USEmployeeInterface):

    def __init__(self, id, name, pay_method, yearly_salary):
        super().__init__(id, name, pay_method, yearly_salary)

    def calculate_usd_salary(self) -> Decimal:
        return super().calculate_salary() * Decimal(0.75)
