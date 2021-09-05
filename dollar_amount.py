from vending_machine_error.vending_machine_error import InsufficientFundsError


class DollarAmount(object):
    def __init__(self):
        self.amount = 0
        self.amount_arr = list(str(self.amount))

    def get_amount(self):
        if self.amount > 0:
            self.amount_arr = list(str(self.amount))
            return "$"+self.get_tens() + self.get_ones() + "." + self.get_tenths() + self.get_hundredths()
        return "$0.00"

    def get_tens(self):
        if self.amount > 999:
            return self.amount_arr[len(self.amount_arr) - 4]
        return ""

    def get_ones(self):
        if self.amount > 99:
            return self.amount_arr[len(self.amount_arr) - 3]
        return "0"

    def get_tenths(self):
        if self.amount > 9:
            return self.amount_arr[len(self.amount_arr) - 2]
        return "0"

    def get_hundredths(self):
        return self.amount_arr[len(self.amount_arr) - 1]

    def add_money(self, money_added):
        self.amount += money_added
        return self

    def subtract_money(self, price):
        if price <= self.amount:
            self.amount -= price
            return self
        raise InsufficientFundsError

    def make_balance_zero(self):
        self.amount = 0
