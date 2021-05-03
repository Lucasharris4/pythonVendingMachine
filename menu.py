from VendingMachineError import InvalidSelectionError, OutOfStockError


class MenuInterface(object):
    def get_item_by_code(self, code):
        raise NotImplementedError

    def to_string(self):
        raise NotImplementedError


class MenuImp(MenuInterface):
    def __init__(self):
        self.menu = {'A1': {'name': 'lays', 'price': '3.75', 'stock': 0},
                     'B3': {'name': 'pepsi', 'price': '1.75', 'stock': 10},
                     'C4': {'name': 'payday', 'price': '.99', 'stock': 10}, }

    def get_item_by_code(self, code):
        try:
            return self.pull_item_out_of_stock(code)
        except KeyError:
            raise InvalidSelectionError

    def pull_item_out_of_stock(self, code):
        if self.menu[code]['stock'] > 0:
            self.menu[code]['stock'] -= 1
            return self.menu[code]
        raise OutOfStockError

    def to_string(self):
        return str(self.menu)