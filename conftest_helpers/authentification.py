from typing import Generator
import pytest

from clients.authentification.authentification_client import AuthentificationClients, get_authentification_client
from helpers.auth_helper import AuthentificationFixture
from helpers.auth_helper import create_user_context


@pytest.fixture
def authentification_client() -> AuthentificationClients:
    return get_authentification_client()

@pytest.fixture
def function_auth(authentification_client: AuthentificationClients) -> Generator[AuthentificationFixture, None, None]:
    with create_user_context(authentification_client) as user:
        yield user
