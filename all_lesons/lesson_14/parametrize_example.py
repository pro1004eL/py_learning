import pytest


class BaseValues:

    # def __init__(self):
    #     self.data = None
    def get_data(self):
        return self.data

class PositiveValues(BaseValues):
    data = [1,2,3,5]


class NegativeValues(BaseValues):
    data = ['24', True, None, {1,3}]

@pytest.mark.parametrize('value', PositiveValues().get_data())
def test_positive_something(value):
    pass

@pytest.mark.parametrize('value', NegativeValues().get_data())
def test_negative_something(value):
    pass


