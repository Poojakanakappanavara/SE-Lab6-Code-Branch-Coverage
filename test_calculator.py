
from calculator import calculate_discount


def test_member_expensive_item():
    result = calculate_discount(150, True)
    assert result == 150 * 0.85
