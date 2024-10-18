import allure
import locators
from conftest import register_and_remove_user
import data
from api import Api


class TestCreateUser:

    @allure.title('Проверка создания пользователя с валидными данными')
    def test_registration_with_valid_data(self, register_and_remove_user):
        register_user_response = register_and_remove_user
        assert register_user_response.status_code == 200
        assert register_user_response.json()['accessToken'] != ''

    @allure.title('Проверка возможности создания пользователя, который уже есть в базе данных')
    def test_register_already_existing_user(self):
        response = Api.register_user(data.User.existing_user_data)
        assert response.status_code == 403
        assert response.json()['message'] == locators.Response.USER_ALREADY_EXISTS
        assert not response.json()['success']

    @allure.title('Проверка появления ошибки при создании пользователя, если не заполнено обязательное поле password')
    def test_registration_password_field_is_not_filled(self):
        register_user_response = Api.register_user(data.User.new_user_data_with_empty_field)
        assert register_user_response.status_code == 403
        assert register_user_response.json()['message'] == locators.Response.REQUIRED_FIELDS_MISSING
        assert not register_user_response.json()['success']
