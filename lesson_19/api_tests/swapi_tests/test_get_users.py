import requests
import pytest

from core.api.swapi.swapi_contoller import SwapiController

swapi_ctrl = SwapiController()


@pytest.mark.swapi
def test_get_users():
    response = swapi_ctrl.get_people()

    assert response.status_code == 200, f'Expected status code 200, actual is {response.status_code}'


@pytest.mark.swapi
@pytest.mark.parametrize('page_number', [1,2,5, 10])
def test_get_users_pages(page_number):

    response = swapi_ctrl.get_people(params={'page': page_number})

    responce_data = response.json()
    next_page_value = responce_data['next']
    last_number = next_page_value.split('=')[-1]  # ["https://swapi.dev/api/people/?page", '2']

    assert int(last_number) == page_number+1

