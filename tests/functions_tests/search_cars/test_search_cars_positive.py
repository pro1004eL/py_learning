import pytest

from all_lesons.lesson_8.search_cars import search_cars

@pytest.mark.searchcar
def test_no_matching_cars_positive():
    actual_result = search_cars(2017,1.5,5000)
    expected_result = 'No matching cars.'
    assert (actual_result, expected_result)

@pytest.mark.searchcar
def test_search_cars_positive():
    actual_result = search_cars(2017,2.5,35000)
    expected_result = 'Nissan Titan: Color: silver, Year: 2018, Engine Volume: 5.6, Type: pickup, Price: 35000'
    assert (actual_result, expected_result)











