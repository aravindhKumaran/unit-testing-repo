import pytest 
import source.shapes as shapes

# Using global fixtures (conftest.py) and functions instead of Classes



def test_area(rectangle_obj):
    assert rectangle_obj.area() == 10 * 20
        
def test_perimeter(rectangle_obj):
    assert rectangle_obj.perimeter() == (10 * 2) + (20 * 2)