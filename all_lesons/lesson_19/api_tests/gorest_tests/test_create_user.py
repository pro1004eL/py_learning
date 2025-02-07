from core.api.gorest.gorest_contoller import GorestController
import time


def test_create_user():

    user_data = {"name":"Tenali Ramakrishna",
                 "gender":"male",
                 "email":f"tenali.ramakrishna@{time.time()}.com",
                 "status":"active"}

    GorestController().create_user(data=user_data)


def test_create_user_auth_negative():

    user_data = {"name":"Tenali Ramakrishna",
                 "gender":"male",
                 "email":f"tenali.ramakrishna@{time.time()}.com",
                 "status":"active"}

    GorestController().create_user(data=user_data, token='ggwp', status_code=401)




