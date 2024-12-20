

def test_get_current_positive_some_feature(qa_auto_ctrl):  # викликаємо інтанс qa_auto_ctrl
    response_current = qa_auto_ctrl.get_current().json()  # використовуємо інтанс qa_auto_ctrl

    assert response_current['status'] == 'ok'
