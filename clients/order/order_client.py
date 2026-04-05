from requests import Response
import allure

from clients.private_http_builder import AuthentificationUserSchema, get_private_http_client
from clients.order.order_schema import CreateOrderRequestSchema
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from tools.routes import AppRoute


class OrderClients(ApiClient):
    @allure.step("Create order")
    def create_order_api(self, request: CreateOrderRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.CREATE_ORDER, json=request_data)
    
def get_order_client(user: AuthentificationUserSchema) -> OrderClients:
    return OrderClients(client=get_private_http_client(user=user))

def get_public_order_client() -> OrderClients:
    return OrderClients(client=get_public_http_client())