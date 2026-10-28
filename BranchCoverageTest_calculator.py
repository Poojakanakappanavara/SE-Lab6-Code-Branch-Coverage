
from calculator import calculate_discount


def test_member_expensive_item():
    assert calculate_discount(150, True) == 150 * 0.85


def test_non_member_expensive_item():
    assert calculate_discount(150, False) == 150 * 0.95


def test_member_cheap_item():
    assert calculate_discount(80, True) == 80 * 0.90


def test_non_member_cheap_item():
    assert calculate_discount(80, False) == 80
