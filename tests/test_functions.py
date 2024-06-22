import pytest
import time 
from typing import * 
import source.functions as F


def test_add():
    actual_result = F.add(number_one=2, number_two=4)
    assert actual_result == 6


def test_add_strings():
    actual_result = F.add(number_one="i like ", number_two="cars")
    assert actual_result == "i like cars"


def test_divide():
    actual_result = F.divide(number_one=4, number_two=2)
    assert actual_result == 2


def test_divide_by_zero():
    """ Raise ZeroDivisionError """
    with pytest.raises(ValueError):
        F.divide(number_one=4, number_two=0)


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    actual_result = F.divide(number_one=4, number_two=2)
    assert actual_result == 2


@pytest.mark.skip(reason="This feature is currently broken")
def test_add_skip():
    actual_result = F.add(number_one=2, number_two=4)
    assert actual_result == 6


@pytest.mark.xfail(reason="We know we cnnot divide by zero")
def test_divide_by_zero_broken():
    F.divide(number_one=4, number_two=0)