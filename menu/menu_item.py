from vending_machine.vending_machine_error import OutOfStockError, InvalidSelectionError, Message


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

    def put_item_back(self):
        self.info['stock'] += 1
        return self

    def get_price_in_pennies(self):
        return int(self.info['price'].replace('.', ''))

    def to_string(self):
        return self.info['code'] + ": " +\
               self.info['name'] + " $" +\
               self.info['price'] +\
               self.in_or_out_of_stock() + "\n"

    def in_or_out_of_stock(self):
        if self.info['stock'] == 0:
            return " " + Message.OUT_OF_STOCK
        return ""


class ItemList(object):
    def __init__(self, *items):
        self.list = []
        for arg in items:
            self.list.append(arg)

    def __getitem__(self, code):
        for item in self.list:
            if item.info['code'] == code:
                return item
        raise InvalidSelectionError

    def to_string(self):
        result = ""
        for item in self.list:
            result += item.to_string()
        return result
