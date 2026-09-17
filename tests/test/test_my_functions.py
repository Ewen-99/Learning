import pytest
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 2)
    assert result == 3

def test_divide():
    result = my_functions.divide(10, 2)
    assert result == 5

def test_divide_by_zero():
#    result = my_functions.divide(10, 0)
#    assert True
    with pytest.raises(ZeroDivisionError):
        result = my_functions.divide(10, 0)
