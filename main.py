from HourlyEmployee import *
from USSalaryEmployee import *
from PayMethod import *
from CurrencyUtils import *

se1 = SalaryEmployee(1, "Brendan", PayMethod.CASH, Decimal(90000))
he1 = HourlyEmployee(2, "Jane", PayMethod.CHECK, Decimal(5.00))
USe1 = USSalaryEmployee(3, "US Guy", PayMethod.CASH, Decimal(95000))

employee_list = [se1, he1, USe1]

for e in employee_list:

    print(e.name)

    if isinstance(e, USEmployeeInterface):
        print(output_currency(e.calculate_usd_salary()) + " (USD)")
    else:
        print(output_currency(e.calculate_salary()))

    print(f"Pay method is {e.pay_method.name}")

    print("*" * 50)
