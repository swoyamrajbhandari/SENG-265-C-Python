from ..src.modules import math


def test_fibonacci():
    tests: list = [(0, 0), (1, 0), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)]
    for test in tests:
        n: int = test[0]
        expected: float = float(test[1])
        result: float = math.sample_function_fibonacci(n)
        assert result == expected, f'fibonacci({n}) should be: {expected}, got: {result}'


def test_fibonacci_invalid_input():
    n = -10
    expected = -1
    result = math.sample_function_fibonacci(n)
    assert result == expected, f'fibonacci({n}) should be: {expected}, got: {result}'
