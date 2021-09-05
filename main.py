import json
from controller.lambda_controller import *
from controller.vending_machine_controller import *
from menu.menu import *
from test.lambda_event import lambda_event
from testing_constants_vm import *
from vending_machine.vending_machine import *


def vending_machine_handler(event, context):
    vending_machine = VendingMachine(MenuImp(items))
    vending_machine_controller = VendingMachineController(vending_machine)
    lambda_controller = LambdaController(vending_machine_controller)
    return {
        'statusCode': 200,
        'body': json.dumps({
                        'response': lambda_controller.execute(event)
        })
    }


if __name__ == '__main__':
    print (vending_machine_handler(lambda_event, None))
