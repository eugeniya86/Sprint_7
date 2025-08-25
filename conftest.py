import pytest
from helpers import login_courier, register_new_courier_and_return_login_password, delete_courier


@pytest.fixture
def setup_courier():
    courier_data = register_new_courier_and_return_login_password()
    yield courier_data
    if courier_data:
        login, password, _ = courier_data
        login_courier(login, password)
        delete_courier(login, password)
