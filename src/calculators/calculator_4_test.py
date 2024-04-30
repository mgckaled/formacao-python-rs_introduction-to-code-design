from typing import Dict, List

from src.drivers.interfaces.driver_handler_interface import \
    DriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler

from .calculator_4 import Calculator4


class MockRequest:

    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, number: List[float]) -> float:
        pass

    def variance(self, number: List[float]) -> float:
        pass

    def mean(self, number: List[float]) -> float:
        pass


def test_calculate_integration():
    mock_request = MockRequest({
        "numbers": [30.1, 40.5, 50.0]
    })

    driver = NumpyHandler()
    calculator_4 = Calculator4(driver)
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 4, 'result': 40.2}}


def test_calculate():
    mock_request = MockRequest({
        "numbers": [30.1, 40.5, 50.0]
    })

    driver = MockDriverHandler()
    calculator_4 = Calculator4(driver)
    formated_response = calculator_4.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 4, 'result': 40.2}}
