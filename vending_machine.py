class DollarAmount(object):

    def __init__(self):
        self.amount = 0

    def get_amount(self):
        print('amount', self.amount)
        if self.amount == 0:
            return "0.00"
        return "0." + str(self.amount)

    def add_money(self, money_added):
        self.amount += money_added


class VendingMachine(object):
    def __init__(self):
        self.balance = DollarAmount()

    def insert_quarter(self):
        self.balance.add_money(25)

    def get_change(self):
        return self.balance.get_amount()
