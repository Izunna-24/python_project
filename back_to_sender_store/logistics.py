class BLogistics:
    def __init__(self):
        self.base_pay = 5000

    def hasriders(self):
        return True

    def daily_payment(self, deliveries):
        rider_wage = self.base_pay

        if deliveries < 0:
            raise ValueError("No deliveries made!")
        elif deliveries > 100:
            raise ValueError("Deliveries exceeded per day!!")
        elif deliveries <= 50:
            rider_wage += deliveries * 160
        elif deliveries <= 59:
            rider_wage += deliveries * 200
        elif deliveries <= 69:
            rider_wage += deliveries * 250
        else:
            rider_wage += deliveries * 500

        return rider_wage
