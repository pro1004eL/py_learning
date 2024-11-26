import requests
import logging

logger = logging.getLogger('RestBase')

class RestBase:
    @staticmethod
    def _execute_request(method, url, params=None, data=None, json=None, headers=None, files=None):

        responce = getattr(requests, method)(url=url, params=params, data=data,
                                   json=json, headers=headers, files=files)

        logger.info(f'request was sent to {method} {url} with params {params}'
                    f'\n Response has status {responce.status_code}')

        return responce