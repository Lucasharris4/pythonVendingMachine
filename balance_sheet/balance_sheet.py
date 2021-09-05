from dollar_amount import DollarAmount


class BalanceSheet(object):
    def __init__(self, **kwargs):
        self.revenue = kwargs.get('revenue', DollarAmount())
        self.balance = kwargs.get('balance', DollarAmount())
        self.sales = {}
        self.credits = []
        self.debits = []

    def get_revenue(self):
        return self.revenue.get_amount()

    def get_balance(self):
        return self.balance.get_amount()

    def add_transaction(self, transaction):
        transaction.record(self)

    def get_sales_for_menu_item(self, item):
        try:
            return self.sales[item.info['name']]
        except KeyError:
            return 0
