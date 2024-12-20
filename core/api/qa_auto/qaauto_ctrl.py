from core.api.rest_base import RestBase
from settings import settings

base_url = settings.QAAUTO_BASE_API_URL


class QAAutoCtrl(RestBase):

    def __init__(self, url=base_url):
        self.url = url
        self.cookies = None

    def login(self, json=None, status_code=200):
        """
        send request to get  /auth/signin
        """
        url = f'{self.url}/auth/signin'

        response = self._execute_request(method='post', url=url, json=json, status_code=status_code)
        self.cookies = dict(response.cookies)

        return response

    def get_current(self, status_code=200, use_cookies=True):
        """
        send request to get  /users/current
        """
        url = f'{self.url}/users/current'

        cookies = self.cookies if use_cookies else None

        return self._execute_request(method='get', url=url, status_code=status_code, cookies=cookies)

    def get_profile(self, status_code=200, use_cookies=True):
        """
        send request to get  /users/profile
        """
        url = f'{self.url}/users/profile'

        cookies = self.cookies if use_cookies else None

        return self._execute_request(method='get', url=url, status_code=status_code, cookies=cookies)
