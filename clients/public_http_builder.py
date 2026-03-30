from requests_toolbelt import sessions
from requests import Session

from tools.routes import AppRoute


def get_public_http_client() -> Session:
    return sessions.BaseUrlSession(base_url=AppRoute.BASE_URL)