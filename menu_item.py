from vending_machine_error import OutOfStockError, InvalidSelectionError


class MenuItem(object):
    def __init__(self):
        self.info = {
            "code": "XX",
            "name": "",
            "price": "0.00",
            "stock": 0,
        }

    def __setitem__(self, key, value):
        self.info[key] = value
        return self

    def pull_item_out_of_stock(self):
        if self.info['stock'] > 0:
            self.info['stock'] -= 1
            return self
        raise OutOfStockError


class ItemList(object):
    def __init__(self, *args):
        self.list = []
        for arg in args:
            self.list.append(arg)

    def __getitem__(self, code):
        for item in self.list:
            if item.info['code'] == code:
                return item
        raise InvalidSelectionError
