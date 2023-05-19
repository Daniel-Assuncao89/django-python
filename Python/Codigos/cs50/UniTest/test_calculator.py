from calculator import square


def test_posite():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-3) == 9
    assert square(-2) == 4


def test_zero():
    assert square(0) == 0
