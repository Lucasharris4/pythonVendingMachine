from dollar_amount import DollarAmount
from enum import Enum


class Message(Enum):
    OUT_OF_STOCK = "Out of Stock"
    INVALID_SELECTION = "Invalid Selection"
    INSUFFICIENT_FUNDS = "Insufficient Funds"


class VendingMachine(object):
    menu = {'A1': {'name': 'lays', 'price': '3.75', 'stock': 0},
            'B3': {'name': 'pepsi', 'price': '1.75', 'stock': 10},
            'C4': {'name': 'payday', 'price': '.99', 'stock': 10},}


    def __init__(self):
        self.balance = DollarAmount()

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
        return str(self.menu)

    def make_selection(self, selection):
        try:
            menu_item = self.menu[selection]
            return self.make_purchase(menu_item)
        except KeyError:
            return Message.INVALID_SELECTION

    def make_purchase(self, menu_item):
        price = int(menu_item['price'].replace('.', ''))
        if price > self.balance.amount:
            return Message.INSUFFICIENT_FUNDS
        if menu_item['stock'] == 0:
            return Message.OUT_OF_STOCK
        return Message.OUT_OF_STOCK
