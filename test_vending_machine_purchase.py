import unittest

from menu import MenuImp
from testing_constants_vm import *
from vending_machine import VendingMachine


class TestPurchase(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine(MenuImp(items))

    def test_stock_depletes_after_successful_purchase(self):
        self.vm.insert_five()
        self.vm.make_selection(drink)
        self.assertTrue('9'.__eq__(self.vm.menu.items.__getitem__(drink).info['stock']))

    def test_balance_depletes_after_successful_purchase(self):
        self.vm.insert_five()
        self.vm.make_selection(drink)
        self.assertEqual('3.25', self.vm.balance.get_amount())
