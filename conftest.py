import pytest
import requests
from helpers import BASE_URL, login_courier, register_new_courier_and_return_login_password


@pytest.fixture
def setup_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data
    if courier_data:
        login, password, _ = courier_data
        response = login_courier(login, password)
        if response.status_code == 200:
            courier_id = response.json()["id"]
            requests.delete(f'{BASE_URL}/courier/{courier_id}')
