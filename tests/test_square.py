import pytest 
import source.shapes as shapes 

# Parametrize tests

@pytest.fixture 
def square_obj():
    return shapes.Square(side_length = 5)


def test_area(square_obj):
    assert square_obj.area() == 25

@pytest.mark.parametrize("side_length, expected_area", [(5, 25), (4, 16), (2, 4)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter