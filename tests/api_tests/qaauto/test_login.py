from core.api.qa_auto.qaauto_ctrl import QAAutoCtrl
from settings import settings

qa_auto_ctrl = QAAutoCtrl()


def test_login_positive():
    print('send request to login')
    qa_auto_ctrl.login({
        "email": settings.USER_EMAIL,
        "password": settings.USER_PASSWORD,
        "remember": False
    })
    yield
    print('Runs after test')
