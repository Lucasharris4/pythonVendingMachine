class MenuInterface(object):
    def get_item_by_code(self, code):
        raise NotImplementedError

    def to_string(self):
        raise NotImplementedError


class MenuImp(MenuInterface):

    def __init__(self, items):
        self.items = items

    def get_item_by_code(self, code):
        return self.items.__getitem__(code).pull_item_out_of_stock()

    def to_string(self):
        return self.items.to_string()
