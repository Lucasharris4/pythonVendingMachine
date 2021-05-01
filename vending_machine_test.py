import unittest

from vending_machine import VendingMachine


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.vm = VendingMachine()

    def test_no_change_if_no_money_inserted(self):
        self.assertEqual("0.00", self.vm.get_change())

    def test_insert_quarter(self):
        self.vm.insert_quarter()
        self.assertEqual("0.25", self.vm.get_change())

    def test_insert_two_quarters(self):
        self.vm.insert_quarter()
        self.vm.insert_quarter()
        self.assertEqual(self.vm.get_change(), "0.50")


if __name__ == '__main__':
    unittest.main()
