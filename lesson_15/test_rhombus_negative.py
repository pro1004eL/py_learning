import pytest

from lesson_15.homework_15_1 import Rhombus

# @pytest.mark.parametrize('side_a','angle_a', 'expected_angle_b', [
#     (5, 60, 120),      # Valid case: corner_a + corner_b = 180
#     (10, 90, 90),      # Valid case: right angles (90, 90)
#     (3, 45, 135),
# ])
# def test_rhombus_positive_values(side_a, angle_a, expected_angle_b):
#
#     rhombus = Rhombus(side_a, angle_a)
#
#     assert rhombus.side_a == side_a
#     assert rhombus.angle_a == angle_a
#     assert rhombus.angle_b == expected_angle_b

@pytest.mark.parametrize("side_a, expected_error", [
    ('0', TypeError),
    (-1, ValueError),
    (0, ValueError),
    (None, TypeError)
], ids=['string_value','negative_value', '0', 'None'])

def test_rhombus_invalid_side_a(side_a, expected_error):
    with pytest.raises(expected_error):
        Rhombus(side_a, 10)

@pytest.mark.parametrize("angle_a, expected_error", [
    (0, ValueError),
    (180, ValueError),
    ('10', TypeError),
    (-10, ValueError),
    (None, TypeError)
], ids=['0', '180', 'string value', 'negative value', 'None'])

def test_rhombus_invalid_angle_a(angle_a, expected_error):
    with pytest.raises(expected_error):
        Rhombus(5, angle_a)

