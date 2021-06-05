import unittest

from testing_constants_vm import *
from vending_machine.vending_machine_error import PyVendingMachineError, Message
from vending_machine.vending_machine import VendingMachine
from menu.menu import MenuImp


class TestMenu(unittest.TestCase):
    def setUp(self):
        menu = MenuImp(items)
        self.vm = VendingMachine(menu)
        self.menu = test_menu

    def test_print_menu(self):
        expected = "A1: lays $3.75 Out of Stock\n" + \
                   "B3: pepsi $1.75\n" + \
                   "C4: payday $0.99\n"
        self.assertEqual(expected, self.vm.print_menu())

    def test_invalid_selection(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.make_selection("XX")
        self.assertEqual(context.exception.message, Message.INVALID_SELECTION)

    def test_insufficient_funds(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.make_selection(drink)
        self.assertEqual(context.exception.message, Message.INSUFFICIENT_FUNDS)

    def test_out_of_stock(self):
        with self.assertRaises(PyVendingMachineError) as context:
            self.vm.insert_five()
            self.vm.make_selection(chips)
        self.assertEqual(context.exception.message, Message.OUT_OF_STOCK)


if __name__ == '__main__':
    unittest.main()
