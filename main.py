import json

from balance_recorder.s3_balance_recorder import S3BalanceRecorder
from controller.lambda_controller import *
from controller.vending_machine_controller import *
from menu.menu import *
from test.lambda_event import lambda_event
from testing_constants_vm import *
from vending_machine.vending_machine import *


vending_machine = VendingMachine(MenuImp(items))
vending_machine_controller = VendingMachineController(vending_machine)
balance_recorder = S3BalanceRecorder(bucket="vendingmachinerecords", file_name="balance_sheet.txt")
lambda_controller = LambdaController(vending_machine_controller)


def vending_machine_handler(event, context):
    response = lambda_controller.execute(event)
    balance_recorder.save(vending_machine.balance_sheet)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'response': response
        })
    }


if __name__ == '__main__':
    print (vending_machine_handler(lambda_event, None))
