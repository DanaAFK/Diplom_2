class Response:

    USER_ALREADY_EXISTS = 'User already exists'
    REQUIRED_FIELDS_MISSING = 'Email, password and name are required fields'
    INVALID_EMAIL_OR_PASSWORD = 'email or password are incorrect'
    AUTHORIZATION_REQUIRED = 'You should be authorised'
    REQUIRES_ERROR_INGREDIENTS = 'Ingredient ids must be provided'


class Urls:

    URL = 'https://stellarburgers.nomoreparties.site'
    INGREDIENTS = '/api/ingredients'
    ORDER = '/api/orders'
    REGISTER_USER = '/api/auth/register'
    USER = '/api/auth/user'
    LOGIN = '/api/auth/login'
    ALL_ORDERS = '/api/orders/all'
