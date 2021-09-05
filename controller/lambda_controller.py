class LambdaController(object):
    def __init__(self, vending_machine_controller):
        self.vending_machine_controller = vending_machine_controller

    def execute(self, event):
        if event['httpMethod'] == "POST":
            return self.vending_machine_controller.insert_dollar()
        return self.vending_machine_controller.get()
