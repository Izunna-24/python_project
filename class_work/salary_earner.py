from decimal import Decimal
from inheritance_two import CommissionEmployee


class SalaryEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, nin, sales, rate, base_pay):
        super().__init__(first_name, last_name, nin, sales, rate)
        self.base_pay = base_pay

    @property
    def base_pay(self):
        return self._base_pay

    @base_pay.setter
    def base_pay(self, pay):
        if pay < Decimal(0.0):
            raise ValueError("Invalid pay")
        self._base_pay = pay

    def earning(self):
        return self.base_pay + super().earning()

    def __str__(self):
        return f"{super().__repr__()}\n" \
               f"Salary: {self.base_pay:}\n" \
               f"Salary Earning: {self.earning()}"


izu = SalaryEmployee(first_name="Izu", last_name="Ogeh", nin=420, sales=10000, rate=20, base_pay=500000)
print(izu)
# to check if a class is super or subclass of a class use issubclass(), issuperclass(), isinstance(checks if a class is an instance of a class)
#print(issubclass(SalaryEmployee, CommissionEmployee))
