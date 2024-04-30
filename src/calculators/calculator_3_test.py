from typing import Dict, List

from pytest import raises

from src.calculators.calculator_3 import Calculator3
from src.drivers.interfaces.driver_handler_interface import \
    DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError(DriverHandlerInterface):
    def standard_deviation(self, number: List[float]) -> float:
        pass

    def variance(self, number: List[float]) -> float:
        return 2

    def mean(self, number: List[float]) -> float:
        pass


class MockDriverHandler(DriverHandlerInterface):
    def variance(self, number: List[float]) -> float:
        return 1000000

    def standard_deviation(self, number: List[float]) -> float:
        pass

    def mean(self, number: List[float]) -> float:
        pass


def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(
        excinfo.value) == 'Falha no processo: Variância menor que multiplicação'


def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandler())

    response = calculator_3.calculate(mock_request)

    assert response == {'data': {
        'Calculator': 3,
        'value': 1000000,
        'Success': True,
    }
    }
