import unittest

from balance_sheet.balance_sheet import BalanceSheet
from menu.menu import MenuImp
from testing_constants_vm import *
from vending_machine.vending_machine import VendingMachine
from vending_machine_error.vending_machine_error import PyVendingMachineError


class TestPurchase(unittest.TestCase):
    def setUp(self):
        balance_sheet = BalanceSheet()
        self.vm = VendingMachine(MenuImp(items), balance_sheet=balance_sheet)
        self.vm.menu.items.__getitem__(drink).__setitem__('stock', 10)

    def test_stock_depletes_after_successful_purchase(self):
        self.vm.insert_five()
        self.vm.make_selection(drink)
        self.assertEqual(9, self.vm.menu.items.__getitem__(drink).info['stock'])
        self.assertEqual('$1.75', self.vm.balance_sheet.get_revenue())

    def test_balance_depletes_after_successful_purchase(self):
        self.vm.insert_five()
        self.vm.make_selection(drink)
        self.assertEqual('$3.25', self.vm.balance.get_amount())

    def test_stock_does_not_deplete_if_purchase_fails(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.insert_dollar()
            self.vm.make_selection(drink)
        self.assertEqual(10, self.vm.menu.items.__getitem__(drink).info['stock'])

    def test_balance_does_not_deplete_if_purchase_fails(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.insert_dollar()
            self.vm.make_selection(drink)
        self.assertEqual(100, self.vm.balance.amount)
