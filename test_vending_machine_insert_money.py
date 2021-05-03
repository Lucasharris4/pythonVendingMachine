import unittest

from vending_machine import VendingMachine
from menu import MenuImp


class TestInsertMoney(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine(MenuImp())

    def test_no_change_if_no_money_inserted(self):
        self.assertEqual("0.00", self.vm.get_change())

    def test_insert_quarter(self):
        self.vm.insert_quarter()
        self.assertEqual("0.25", self.vm.get_change())

    def test_insert_two_quarters(self):
        self.vm.insert_quarter()
        self.vm.insert_quarter()
        self.assertEqual("0.50", self.vm.get_change())

    def test_insert_dollar(self):
        self.vm.insert_dollar()
        self.assertEqual("1.00", self.vm.get_change())

    def test_insert_five(self):
        self.vm.insert_five()
        self.assertEqual("5.00", self.vm.get_change())

    def test_insert_twenty(self):
        self.vm.insert_twenty()
        self.assertEqual("20.00", self.vm.get_change())

    def test_insert_all_bills(self):
        self.vm.insert_quarter()
        self.vm.insert_dollar()
        self.vm.insert_five()
        self.vm.insert_twenty()
        self.assertEqual("26.25", self.vm.get_change())

    def test_balance_should_be_zero_after_get_change(self):
        self.vm.insert_twenty()
        self.vm.get_change()
        self.assertEqual("0.00", self.vm.get_change())


if __name__ == '__main__':
    unittest.main()
