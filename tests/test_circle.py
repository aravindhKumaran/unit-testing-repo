import pytest
import source.shapes as shapes
import math
from typing import *
import logging


@pytest.fixture
def logger():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    return logger

class TestCircle:

    def setup_method(self, method: Callable[..., None]) -> None:
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)
        print(f"Circle with radius {self.circle.radius} created")

    def teardown_method(self, method: Callable[..., None]) -> None:
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self, logger) -> None:
        logger.warning(f"Testing area for circle with radius {self.circle.radius}")
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self, logger) -> None:
        logger.info(f"Testing perimeter for circle with radius {self.circle.radius}")
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius 