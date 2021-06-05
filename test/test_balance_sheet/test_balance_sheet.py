import unittest

from balance_sheet.balance_sheet import BalanceSheet
from balance_sheet.transaction import Sale
from dollar_amount import DollarAmount
from testing_constants_vm import pepsi, lays, payday


class TestPurchase(unittest.TestCase):
    def setUp(self):
        self.balance_sheet = BalanceSheet()
        self.pepsi_transaction = Sale(pepsi)
        self.lays_transaction = Sale(lays)
        self.payday_transaction = Sale(payday)

    def test_revenue_starts_at_zero(self):
        self.assertEqual("$0.00", self.balance_sheet.get_revenue())

    def test_revenue_builds_with_sales(self):
        self.balance_sheet.add_transaction(self.pepsi_transaction)
        expected_revenue = DollarAmount()
        expected_revenue.add_money(pepsi.get_price_in_pennies())
        self.assertEqual(expected_revenue.get_amount(), self.balance_sheet.get_revenue())

    def test_sales_gives_zero_if_no_sales(self):
        self.assertEqual(0, self.balance_sheet.get_sales_for_menu_item(pepsi))

    def test_sales_are_tracked(self):
        self.balance_sheet.add_transaction(self.pepsi_transaction)
        self.balance_sheet.add_transaction(self.pepsi_transaction)
        self.balance_sheet.add_transaction(self.pepsi_transaction)

        self.balance_sheet.add_transaction(self.lays_transaction)
        self.balance_sheet.add_transaction(self.lays_transaction)

        self.balance_sheet.add_transaction(self.payday_transaction)

        self.assertEqual(3, self.balance_sheet.get_sales_for_menu_item(pepsi))
        self.assertEqual(2, self.balance_sheet.get_sales_for_menu_item(lays))
        self.assertEqual(1, self.balance_sheet.get_sales_for_menu_item(payday))
