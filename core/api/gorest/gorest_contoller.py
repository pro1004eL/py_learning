from core.api.rest_base import RestBase


class SwapiController(RestBase):

    def __init__(self, url=f'https://swapi.dev/api/'):
        self.url = url

    def get_person(self, user_id, status_code=200):
        '''
        send request to get api/people/{user_id}/
        '''

        url = f'{self.url}people/{user_id}'

        return self._execute_request(method='get', url=url, params = None, status_code=status_code)

    def get_people(self, params = None, status_code=200):
        '''
        send request to get api/people/
        '''

        url = f'{self.url}people/'

        return self._execute_request(method='get', url=url, params=params, status_code=status_code)

