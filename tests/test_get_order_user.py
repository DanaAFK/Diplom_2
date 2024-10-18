import allure
import locators
from conftest import register_and_remove_user
from api import Api


class TestGetOrderUser:

    @allure.title('Авторизованный пользователь может получить заказы конкретного пользователя')
    def test_get_order_user_authorized_user_success(self, register_and_remove_user):
        register = register_and_remove_user
        access_token = register.json()['accessToken']
        get_user_orders_response = Api.fetch_user_orders(access_token)
        assert get_user_orders_response.status_code == 200
        assert get_user_orders_response.json()['orders'] == []
        assert get_user_orders_response.json()['success']

    @allure.title('Неавторизованный пользователь не может получить заказы конкретного пользователя')
    def test_get_order_user_none_user_wrong(self):
        get_user_orders_response = Api.fetch_user_orders('')
        assert get_user_orders_response.status_code == 401
        assert get_user_orders_response.json()['message'] == locators.Response.AUTHORIZATION_REQUIRED
        assert not get_user_orders_response.json()['success']

