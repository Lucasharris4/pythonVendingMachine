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
        menu_item = self.menu.get_item_by_code(selection)
        return self.make_purchase(menu_item)

    def make_purchase(self, menu_item):
        price = int(menu_item['price'].replace('.', ''))
        self.check_for_sufficient_funds(price)

    def check_for_sufficient_funds(self, price):
        if price > self.balance.amount:
            raise InsufficientFundsError
