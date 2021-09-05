class VendingMachineControllerI(object):
    def get(self):
        raise NotImplementedError

    def insert_dollar(self):
        raise NotImplementedError


class VendingMachineController(VendingMachineControllerI):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
        pass

    def get(self):
        return self.vending_machine.print_menu()

    def insert_dollar(self):
        return self.vending_machine.insert_dollar()
