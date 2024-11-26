import requests
import pytest

from core.api.swapi.swapi_contoller import SwapiController

swapi_ctrl = SwapiController()


@pytest.mark.swapi
@pytest.mark.parametrize('user_id', [1,2,3], ids=['user_1','user_2','user_3',])
def test_get_user(user_id):

    response = swapi_ctrl.get_person(user_id)

    assert response.status_code == 200, f'Expected status code 200, actual is {response.status_code}'

@pytest.mark.swapi
def test_get_users():
    response = swapi_ctrl.get_people()

    assert response.status_code == 200, f'Expected status code 200, actual is {response.status_code}'




