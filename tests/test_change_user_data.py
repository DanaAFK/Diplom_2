import allure
import locators
from conftest import register_and_remove_user
from api import Api


class TestChangeUserData:

    @allure.title('Изменение email авторизованного пользователя')
    def test_is_possible_to_edit_user_email(self, register_and_remove_user):
        register_user = register_and_remove_user
        access_token = register_user.json()['accessToken']
        user_email = Api.fetch_user_info(access_token).json()['user']['email']
        edit_user_email = Api.update_user_info(body={
            'email': f'test_{user_email}'
        }, token=access_token)
        edited_user_email = Api.fetch_user_info(access_token).json()['user']['email']
        assert edit_user_email.status_code == 200
        assert edited_user_email == f'test_{user_email}'

    @allure.title('ПИзменение username авторизованного пользователя')
    def test_is_possible_to_edit_user_name(self, register_and_remove_user):
        register_user = register_and_remove_user
        access_token = register_user.json()['accessToken']
        user_name = Api.fetch_user_info(access_token).json()['user']['name']
        edit_user_name = Api.update_user_info(body={
            'name': f'test_{user_name}'
        }, token=access_token)
        edited_user_name = Api.fetch_user_info(access_token).json()['user']['name']
        assert edit_user_name.status_code == 200
        assert edited_user_name == f'test_{user_name}'

    @allure.title('Нельзя изменить возможности поменять email, если пользователь не авторизован')
    def test_impossible_to_edit_user_email_not_authorized(self, register_and_remove_user):
        register_user = register_and_remove_user
        access_token = register_user.json()['accessToken']
        user_email = Api.fetch_user_info(access_token).json()['user']['email']
        edit_user_email = Api.update_user_info(body={
            'email': f'test_{user_email}'
        }, token='')
        edited_user_email = Api.fetch_user_info(access_token).json()['user']['email']
        assert edit_user_email.status_code == 401
        assert edited_user_email == user_email
        assert edit_user_email.json()['message'] == locators.Response.AUTHORIZATION_REQUIRED

    @allure.title('Нельзя изменить возможности поменять username, если пользователь не авторизован')
    def test_impossible_to_edit_user_name_not_authorized(self, register_and_remove_user):
        register_user = register_and_remove_user
        access_token = register_user.json()['accessToken']
        user_name = Api.fetch_user_info(access_token).json()['user']['name']
        edit_user_name = Api.update_user_info(body={
            'name': f'test_{user_name}'
        }, token='')
        edited_user_name = Api.fetch_user_info(access_token).json()['user']['name']
        assert edit_user_name.status_code == 401
        assert edited_user_name == user_name
        assert edit_user_name.json()['message'] == locators.Response.AUTHORIZATION_REQUIRED
