import allure
import locators
from conftest import register_and_remove_user
import data
from api import Api


class TestCreateOrder:

    @allure.title('Cоздание заказа , если добавленны ингридиенты и пользователь есть в базе данных')
    def test_create_order_with_authorization_succes(self, register_and_remove_user):
        register_response = register_and_remove_user
        access_token = register_response.json()['accessToken']
        create_order_response = Api.submit_order(access_token, data.Order.order_data)
        assert create_order_response.status_code == 200
        assert create_order_response.json()['success']
        assert create_order_response.json()['order']['ingredients'][0]['_id'] == data.Order.order_data['ingredients'][0]

    @allure.title('Ошибка при создании заказа, если пользователь не авторизован')
    def test_create_order_not_authorized_wrong(self):
        access_token = ''
        create_order_response = Api.submit_order(access_token, data.Order.order_data)
        assert create_order_response.status_code == 200
        assert create_order_response.json()['success']
        assert create_order_response.json()['order']['number'] != ''

    @allure.title('Нельзя создать заказ без ингредиентов ')
    def test_create_order_no_ingredients_wrong(self, register_and_remove_user):
        register_user = register_and_remove_user
        access_token = register_user.json()['accessToken']
        create_order_response = Api.submit_order(access_token, data.Order.order_without_ingredients)
        assert create_order_response.status_code == 400
        assert not create_order_response.json()['success']
        assert create_order_response.json()['message'] == locators.Response.REQUIRES_ERROR_INGREDIENTS

    @allure.title('Нельзя создать заказ, если указан невалидный хэш ингредиентов')
    def test_create_order_invalid_ingredient_hash_wrong(self, register_and_remove_user):
        register_user = register_and_remove_user
        access_token = register_user.json()['accessToken']
        create_order_response = Api.submit_order(access_token, data.Order.invalid_ingredient_data)
        assert create_order_response.status_code == 500
