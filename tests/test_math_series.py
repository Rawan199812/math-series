from math_series import __version__
from math_series.series import fibonacci,sum_series,lucas


def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_one():
    expected = 0
    actual = fibonacci(1)
    assert actual == expected

# def test_fibonacci_negative():
#     expected = "Please enter positive numbers only"
#     actual = fibonacci(-1)
#     assert actual == expected


