import unittest

from testing_constants_vm import *
from vending_machine.vending_machine import VendingMachine
from menu.menu import MenuImp


class TestInsertMoney(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine(MenuImp(items))

    def test_no_change_if_no_money_inserted(self):
        self.assertEqual(zero_balance, self.vm.get_change())

    def test_insert_quarter(self):
        self.vm.insert_quarter()
        self.assertEqual(quarter, self.vm.get_change())

    def test_insert_two_quarters(self):
        self.vm.insert_quarter()
        self.vm.insert_quarter()
        self.assertEqual(fifty_cent, self.vm.get_change())

    def test_insert_dollar(self):
        self.vm.insert_dollar()
        self.assertEqual(dollar, self.vm.get_change())

    def test_insert_five(self):
        self.vm.insert_five()
        self.assertEqual(five, self.vm.get_change())

    def test_insert_twenty(self):
        self.vm.insert_twenty()
        self.assertEqual(twenty, self.vm.get_change())

    def test_insert_all_bills(self):
        self.vm.insert_quarter()
        self.vm.insert_dollar()
        self.vm.insert_five()
        self.vm.insert_twenty()
        self.assertEqual(all_currency, self.vm.get_change())

    def test_balance_should_be_zero_after_get_change(self):
        self.vm.insert_twenty()
        self.vm.get_change()
        self.assertEqual(zero_balance, self.vm.get_change())


if __name__ == '__main__':
    unittest.main()
