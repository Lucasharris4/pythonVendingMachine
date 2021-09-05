class LambdaController(object):
    def __init__(self, vending_machine_controller):
        self.vending_machine_controller = vending_machine_controller

    def execute(self, event):
        return self.vending_machine_controller.get()