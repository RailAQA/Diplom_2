from enum import Enum


class AppRoute(str, Enum):
    BASE_URL = "https://stellarburgers.education-services.ru"
    LOGIN_USER = "/api/auth/login"
    CREATE_USER = "/api/auth/register"
    CREATE_ORDER = "/api/orders"
    DELETE_USER = "/api/auth/user"
    GET_INGREDIENTS = "/api/ingredients"