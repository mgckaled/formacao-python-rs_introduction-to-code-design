from typing import Dict, List

from src.drivers.interfaces.driver_handler_interface import \
    DriverHandlerInterface
from src.drivers.numpy_handler import NumpyHandler

from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, number: List[float]) -> float:
        return 3

    def variance(self, number: List[float]) -> float:
        pass


def test_calculate_integration():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
    })  # type: ignore

    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.08}}


def test_calculate():
    mock_request = MockRequest({
        "numbers": [2.12, 4.62, 1.32]
    })

    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    formated_response = calculator_2.calculate(mock_request)

    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'result': 0.33}}
