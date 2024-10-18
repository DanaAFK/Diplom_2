import requests
import allure
import locators


class Api:

    @staticmethod
    @allure.step('Отправить запрос на регистрацию пользователя')
    def register_user(body):
        return requests.post(f'{locators.Urls.URL}{locators.Urls.REGISTER_USER}',
                             json=body)

    @staticmethod
    @allure.step('Отправить запрос на удаление пользователя')
    def remove_user(token):
        return requests.delete(f'{locators.Urls.URL}{locators.Urls.USER}', headers={
            'Authorization': token
        })

    @staticmethod
    @allure.step('Отправить запрос на авторизацию пользователя')
    def login_user(email, password):
        return requests.post(f'{locators.Urls.URL}{locators.Urls.LOGIN}', json={
            "email": email,
            "password": password
        })

    @staticmethod
    @allure.step('Получить данные пользователя')
    def fetch_user_info(token):
        return requests.get(f'{locators.Urls.URL}{locators.Urls.USER}', headers={
            'Authorization': token
        })

    @staticmethod
    @allure.step('Обновить данные пользователя')
    def update_user_info(body, token):
        return requests.patch(f'{locators.Urls.URL}{locators.Urls.USER}', headers={
            'Authorization': token
        },
                              json=body)

    @staticmethod
    @allure.step('Создать заказ')
    def submit_order(token, body):
        return requests.post(f'{locators.Urls.URL}{locators.Urls.ORDER}', headers={
            'Authorization': token
        },
                              json=body)

    @staticmethod
    @allure.step('Получить список ингредиентов')
    def fetch_ingredients(token):
        return requests.get(f'{locators.Urls.URL}{locators.Urls.INGREDIENTS}', headers={
            'Authorization': token
        })

    @staticmethod
    def fetch_all_orders(token):
        return requests.get(f'{locators.Urls.URL}{locators.Urls.ALL_ORDERS}', headers={
            'Authorization': token
        })

    @staticmethod
    def fetch_user_orders(token):
        return requests.get(f'{locators.Urls.URL}{locators.Urls.ORDER}', headers={
            'Authorization': token
        })
