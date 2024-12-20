from core.api.rest_base import RestBase


class GorestController(RestBase):

    def __init__(self, url=f'https://gorest.co.in/public/v2/'):
        self.url = url
        self.token = self.get_token()

    def get_token(self):

        return '93812372e8b6db0b0fb5760b51e890dc4ca8b1053e493ced7a4c46b951e47330'

    def get_user(self, user_id, status_code=200):
        '''
        send request to get /users/
        '''

        url = f'{self.url}users/{user_id}/'

        return self._execute_request(method='get', url=url, params = None, status_code=status_code)

    def get_users(self, status_code=200):
        '''
        send request to get /users/
        '''

        url = f'{self.url}users/'

        return self._execute_request(method='get', url=url, params = None, status_code=status_code)

    def create_user(self, data, status_code=201, token=None):
        '''
        send request to get /users/
        '''

        url = f'{self.url}users/'

        headers = {}
        if token is None:
            headers = {'Authorization': f'Bearer {self.token}'}
        else:
            headers = {'Authorization': token}

        return self._execute_request(method='post',
                                     url=url,
                                     data=data,
                                     status_code=status_code,
                                     headers=headers)

    def update_user(self, user_id, status_code=200):
        '''
        send request to get /users/{user_id}/
        '''

        url = f'{self.url}users/{user_id}'

        return self._execute_request(method='patch', url=url, params = None, status_code=status_code)

    def delete_user(self, user_id, status_code=200):
        '''
        send request to get /users/{user_id}/
        '''

        url = f'{self.url}users/{user_id}'

        return self._execute_request(method='delete', url=url, params = None, status_code=status_code)




