
class Transaction(object):
    def __init__(self):
        pass

    def record(self):
        raise NotImplementedError

    def get_item(self):
        return None


class Sale(Transaction):
    def __init__(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def record(self, balance_sheet):
        balance_sheet.revenue.add_money(self.item.get_price_in_pennies())
        try:
            balance_sheet.sales[self.item.info['name']] += 1
        except KeyError:
            balance_sheet.sales.update({self.item.info['name']: 1})


class Credit(Transaction):
    def __init__(self, amount):
        self.amount = amount

    def record(self, balance_sheet):
        balance_sheet.credits.append(self)
        balance_sheet.balance.add_money(self.amount)


class Debit(Transaction):
    def __init__(self, amount):
        self.amount = amount

    def record(self, balance_sheet):
        balance_sheet.debits.append(self)
        balance_sheet.balance.subtract_money(self.amount)
