from vending_machine_error import InsufficientFundsError
from dollar_amount import DollarAmount


class VendingMachine(object):
    def __init__(self, menu):
        self.balance = DollarAmount()
        self.menu = menu

    def insert_quarter(self):
        self.balance.add_money(25)

    def insert_dollar(self):
        self.balance.add_money(100)

    def insert_five(self):
        self.balance.add_money(500)

    def insert_twenty(self):
        self.balance.add_money(2000)

    def get_change(self):
        change = self.balance.get_amount()
        self.balance.make_balance_zero()
        return change

    def print_menu(self):
        return str(self.menu.to_string())

    def make_selection(self, selection):
        return self.make_purchase(self.menu.get_item_by_code(selection))

    def make_purchase(self, menu_item):
        try:
            self.balance.subtract_money(menu_item.get_price_in_pennies())
        except InsufficientFundsError:
            menu_item.put_item_back()
            raise InsufficientFundsError
