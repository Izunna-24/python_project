from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, nin, sales, rates):
        self._first_name = first_name
        self._last_name = last_name
        self._nin = nin
        self._sales = sales
        self._rates = rates

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def nin(self):
        return self._nin

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        if value < Decimal(0.0):
            raise ValueError(f"Invalid amount{value}")
        self._sales = value

    @property
    def rates(self):
        return self._rates

    @rates.setter
    def rates(self, rate):
        if Decimal(0.0) < rate < Decimal(1.0):
            raise ValueError(f"Invalid rate amount")
        self._rates = rate

    def earning(self):
        return self._sales * (self.rates / 100)

    def __repr__(self):
        return f" First Name: {self._first_name}\n Last Name: {self._last_name}\n" \
               f" Nin: {self._nin}\n Earning: {self.earning()}"


bioke = CommissionEmployee(first_name="abbey", last_name="hanna", nin=427, sales=400, rates=5.0)
print(bioke)
