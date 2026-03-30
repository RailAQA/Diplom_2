from requests import Response

from clients.private_http_builder import AuthentificationUserSchema, get_private_http_client
from clients.order.order_schema import CreateOrderRequestSchema
from clients.api_client import ApiClient
from tools.routes import AppRoute


class OrderClients(ApiClient):
    def login_user_api(self, request: CreateOrderRequestSchema) -> Response:
        request_data = request.model_dump()
        return self.post(url=AppRoute.CREATE_ORDER, json=request_data)
    
def get_order_client(user: AuthentificationUserSchema) -> OrderClients:
    return OrderClients(client=get_private_http_client(user=user))