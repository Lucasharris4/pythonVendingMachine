import unittest

from controller.vending_machine_controller import VendingMachineController, VendingMachineControllerI
from vending_machine.vending_machine import VendingMachineI


class ControllerTest(unittest.TestCase):
    def test_get_calls_get_menu(self):
        vending_machine = MockVM()
        self.controller = VendingMachineController(vending_machine)
        self.controller.get()
        self.assertTrue(vending_machine.print_menu_called)


if __name__ == '__main__':
    unittest.main()


class MockVM(VendingMachineI):
    def __init__(self):
        self.print_menu_called = False

    def print_menu(self):
        self.print_menu_called = True

