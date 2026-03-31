from clients.order.order_client import OrderClients, get_order_client, get_public_order_client
from fixtures.authentification import AuthentificationFixture

import pytest


@pytest.fixture
def order_client(function_auth: AuthentificationFixture) -> OrderClients:
    return get_order_client(user = function_auth.authentification_user)

@pytest.fixture
def public_order_client() -> OrderClients:
    return get_public_order_client()