import pytest

from power import power, times, devide


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8, "This should be 8"
    # self.assertEqual(power(base, exp), 8)
    with pytest.raises(TypeError):
        power("2", "3")

def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6, "This should be 6"
    # self.assertEqual(times(num1, num2), 6)


def test_devide():
    num1 = 6
    num2 = 3
    assert devide(num1, num2) == 2, "This should be 2"

def test_devide_by_zero():
    num1 = 6
    num2 = 0
    with pytest.raises(ValueError):
        devide(num1, num2)
    # self.assertRaises(ValueError, devide, num1, num2)
