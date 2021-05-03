import unittest

from VendingMachineError import PyVendingMachineError, Message
from vending_machine import VendingMachine
from menu import MenuImp


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine(MenuImp())
        self.chips = {'name': 'lays', 'price': '3.75'},
        self.drink = {'name': 'pepsi', 'price': '1.75'},
        self.candy_bar = {'name': 'payday', 'price': '.99'},

        self.menu = {'A1': {'name': 'lays', 'price': '3.75', 'stock': 0},
            'B3': {'name': 'pepsi', 'price': '1.75', 'stock': 10},
            'C4': {'name': 'payday', 'price': '.99', 'stock': 10},}

    def test_print_menu(self):
        self.assertEqual(str(self.menu), self.vm.print_menu())

    def test_invalid_selection(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.make_selection("XX")
        self.assertEqual(context.exception.message, Message.INVALID_SELECTION)

    def test_insufficient_funds(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.make_selection("B3")
        self.assertEqual(context.exception.message, Message.INSUFFICIENT_FUNDS)

    def test_out_of_stock(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.insert_five()
            self.vm.make_selection("A1")
        self.assertEqual(context.exception.message, Message.OUT_OF_STOCK)


if __name__ == '__main__':
    unittest.main()
