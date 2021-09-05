import unittest

from controller.lambda_controller import LambdaController
from controller.vending_machine_controller import VendingMachineControllerI


class LambdaControllerTest(unittest.TestCase):
    def test_execute_get_when_lambda_event_calls_get(self):
        mock_event = {
            'httpMethod': 'GET',
            'path': '/',
        }
        self.controller = MockController()
        self.lambda_controller = LambdaController(self.controller)
        self.lambda_controller.execute(mock_event)
        self.assertTrue(self.controller.get_called)

    def test_execute_post_insert_dollar(self):
        mock_event = {
            'httpMethod': 'POST',
            'path': '/insert/dollar',
        }
        self.controller = MockController()
        self.lambda_controller = LambdaController(self.controller)
        self.lambda_controller.execute(mock_event)
        self.assertTrue(self.controller.insert_dollar_called)


if __name__ == '__main__':
    unittest.main()


class MockController(VendingMachineControllerI):
    def __init__(self):
        self.get_called = False
        self.insert_dollar_called = False

    def get(self):
        self.get_called = True

    def insert_dollar(self):
        self.insert_dollar_called = True
