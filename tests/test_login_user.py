import allure
import locators
from api import Api
import data


class TestLogin:

    @allure.title('Успешная авторизация существующего пользователя')
    def test_existing_user_login_successfully(self):
        response = Api.login_user(
            data.User.existing_user_data['email'],
            data.User.existing_user_data['password']
        )
        assert response.status_code == 200
        assert response.json()['success']
        assert data.User.existing_user_data['email'].lower() in response.json()['user']['email']

    @allure.title('Ошибка при авторизации с неверно заполненными полями')
    def test_auth_with_wrong_email_or_password_error(self):
        response = Api.login_user(
            f'-{data.User.existing_user_data["email"]}',
            f'-{data.User.existing_user_data["password"]}'
        )
        assert response.status_code == 401
        assert not response.json()['success']
        assert response.json()['message'] == locators.Response.INVALID_EMAIL_OR_PASSWORD
