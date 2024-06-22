import pytest 
import source.shapes as shapes
from typing import *

@pytest.fixture
def rectangle_obj() -> object:
    return shapes.Rectangle(length=10, width=20)