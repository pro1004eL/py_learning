from pytest import fixture
from settings import settings
from core.api.qa_auto.qaauto_ctrl import QAAutoCtrl


@fixture(scope='session')
def qa_auto_ctrl():
    yield QAAutoCtrl()  # повертає інстанс, теж саме що qa_ctrl = QAAutoCtrl()


@fixture(scope='session', autouse=True)
def qa_auto_login(qa_auto_ctrl):  # зберігає кукі в інстансі класу qa_auto_ctrl
    qa_auto_ctrl.login({  # перед всіма  тести ми залогінемось
        "email": settings.USER_EMAIL,
        "password": settings.USER_PASSWORD,
        "remember": False
    })






