from typing import List

import numpy


class NumpyHandler:
    def __init__(self) -> None:
        self.__np = numpy

    def standard_variation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
