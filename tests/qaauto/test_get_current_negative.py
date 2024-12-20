

def test_get_current_negative(qa_auto_ctrl):  # викликаємо інтанс qa_auto_ctrl
    response_current = qa_auto_ctrl.get_current(status_code=401, use_cookies=False).json()  # використовуємо інтанс qa_auto_ctrl

    assert response_current['status'] == 'error'
