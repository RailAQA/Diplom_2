from requests import Response

from clients.order.order_schema import CreateOrderRequestSchema
from clients.api_client import ApiClient
from tools.routes import AppRoute


class AuthentificationClients(ApiClient):
    def login_user_api(self, request: CreateOrderRequestSchema) -> Response:
        request_data = request.model_dump()
        return self.post(url=AppRoute.CREATE_ORDER, json=request_data)