from faker import Faker

fake = Faker()


class User:
    existing_user_data = {
        "email": "dana@mail.ru",
        "password": "999999999",
        "name": "Gnom Gnomych"
    }

    new_user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.user_name()
    }

    new_user_data_with_empty_field = {
        "email": fake.email(),
        "password": '',
        "name": fake.user_name()
    }


class Order:
    order_data = {
        "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa73"]
    }

    order_without_ingredients = {"ingredients": []}

    invalid_ingredient_data = {"ingredients": ["29565138066543871", "72961510862410428"]}
