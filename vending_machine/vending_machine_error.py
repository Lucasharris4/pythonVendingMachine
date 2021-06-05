from enum import Enum


class Message(Enum):
    OUT_OF_STOCK = "Out of Stock"
    INVALID_SELECTION = "Invalid Selection"
    INSUFFICIENT_FUNDS = "Insufficient Funds"


class PyVendingMachineError(Exception):
    pass


class InvalidSelectionError(PyVendingMachineError):
    def __init__(self):
        self.message = Message.INVALID_SELECTION


class InsufficientFundsError(PyVendingMachineError):
    def __init__(self):
        self.message = Message.INSUFFICIENT_FUNDS


class OutOfStockError(PyVendingMachineError):
    def __init__(self):
        self.message = Message.OUT_OF_STOCK

