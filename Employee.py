from abc import abstractmethod, ABC
from decimal import Decimal
from PayMethod import PayMethod
from Constants import *
from CurrencyUtils import *

class Employee(ABC):

    def __init__(self, id: int, name: str, pay_method: PayMethod):
        self.id = id
        self.name = name
        self.pay_method = pay_method

    @abstractmethod
    def calculate_salary(self, amount: Decimal):
        if amount > ONLINE_PAYMENT_MAX:
            print(f"Changed payment method from {self.pay_method.name} to {PayMethod.ONLINE.name} since "
                  f"the amount is over {output_currency(ONLINE_PAYMENT_MAX)}")
            self.pay_method = PayMethod.ONLINE
        return amount
