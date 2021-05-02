import unittest

from vending_machine import VendingMachine, Message


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()
        self.chips = {'name': 'lays', 'price': '3.75'},
        self.drink = {'name': 'pepsi', 'price': '1.75'},
        self.candy_bar = {'name': 'payday', 'price': '.99'},

        self.menu = {'A1': {'name': 'lays', 'price': '3.75', 'stock': 0},
            'B3': {'name': 'pepsi', 'price': '1.75', 'stock': 10},
            'C4': {'name': 'payday', 'price': '.99', 'stock': 10},}

    def test_print_menu(self):
        self.assertEqual(self.vm.print_menu(), str(self.menu))

    def test_invalid_selection(self):
        self.assertEqual(Message.INVALID_SELECTION, self.vm.make_selection("XX"))

    def test_insufficient_funds(self):
        self.assertEqual(Message.INSUFFICIENT_FUNDS, self.vm.make_selection("B3"))

    def test_out_of_stock(self):
        self.vm.insert_five()
        self.assertEqual(Message.OUT_OF_STOCK, self.vm.make_selection("A1"))


if __name__ == '__main__':
    unittest.main()
