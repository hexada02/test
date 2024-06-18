from my_funcs import utils
import pytest



@pytest.mark.parametrize('a, b, expected', [(10, 5, 2)])
def test_division(a, b, expected):
    assert utils.division(a, b) == expected

@pytest.mark.parametrize('expected_exception, divider, divisionsble', [(ZeroDivisionError, 0, 5),
                                                         (TypeError, '2', 5)])
def zero_division_with_eror(expected_exception, divider, divisionsble):
    with pytest.raises(expected_exception):
        utils.division(divisionsble, divider)













