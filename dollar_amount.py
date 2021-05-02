class DollarAmount(object):
    def __init__(self):
        self.amount = 0
        self.amount_arr = list(str(self.amount))

    def get_amount(self):
        if self.amount == 0:
            return "0.00"
        self.amount_arr = list(str(self.amount))
        tenths = self.amount_arr[len(self.amount_arr) - 2]
        hundredths = self.amount_arr[len(self.amount_arr) - 1]
        return self.get_tens() + self.get_ones() + "." + tenths + hundredths

    def get_tens(self):
        if self.amount > 999:
            return self.amount_arr[len(self.amount_arr) - 4]
        return ""

    def get_ones(self):
        if self.amount > 99:
            return self.amount_arr[len(self.amount_arr) - 3]
        return "0"

    def add_money(self, money_added):
        self.amount += money_added

    def make_balance_zero(self):
        self.amount = 0
