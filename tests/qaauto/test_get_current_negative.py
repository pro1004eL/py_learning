from pytest import fixture

from core.api.local_sqlite.qaauto_ctrl import QAAutoCtrl
from settings import settings

qa_auto_ctrl = QAAutoCtrl()


@fixture(scope='session', autouse=True)
def login():
    print('send request to login')
    qa_auto_ctrl.login({
        "email": settings.USER_EMAIL,
        "password": settings.USER_PASSWORD,
        "remember": False
    })
    yield
    print('Runs after test')


def test_get_current_positive():

    response_current = qa_auto_ctrl.get_current().json()

    assert response_current['status'] == 'ok'

def test_get_profile_positive():

    response_current = qa_auto_ctrl.get_profile().json()

    assert response_current['status'] == 'ok'


def test_get_current_negative():

    response_current = qa_auto_ctrl.get_current(status_code=401, use_cookies=False).json()

    assert response_current['status'] == 'error'







# def get_cookie():
#     body = {
#         "email": settings.user_email,
#         "password": settings.user_password,
#         "remember": False
#     }
#
#     url_sign_in = f'{base_url}/auth/signin'
#
#     # session = requests.Session()
#     # responce_sign_in = session.post(url=url_sign_in, json=body)  # отримуємо cookies
#     #session.cookies.clear()  # чистити кукі для сесії
#
#     responce_sign_in = requests.post(url=url_sign_in, json=body)  # отримуємо cookies
#     cookie = dict(responce_sign_in.cookies)
#
#     return cookie


