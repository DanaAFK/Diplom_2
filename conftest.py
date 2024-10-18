import pytest
import requests
from api import Api
import locators
import data


@pytest.fixture
def remove_user():
    def _remove_user(token):
        Api.remove_user(token)
    yield _remove_user


@pytest.fixture
def register_and_remove_user():
    user_registration_response = Api.register_user(data.User.new_user_data)
    access_token = user_registration_response.json()['accessToken']

    yield user_registration_response

    requests.delete(f'{locators.Urls.URL}{locators.Urls.USER}', headers={
        'Authorization': access_token
    })
