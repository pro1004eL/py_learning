



def test_get_current_positive(qa_auto_ctrl):  # викликаємо інтанс qa_auto_ctrl

    # session = requests.Session()
    #     # responce_sign_in = session.post(url=url_sign_in, json=body)  # отримуємо cookies
    #     #session.cookies.clear()  # чистити кукі для сесії

    response_current = qa_auto_ctrl.get_current().json()  # використовуємо інтанс qa_auto_ctrl

    assert response_current['status'] == 'ok'


def test_get_profile_positive(qa_auto_ctrl):

    response_current = qa_auto_ctrl.get_profile().json()

    assert response_current['status'] == 'ok'


