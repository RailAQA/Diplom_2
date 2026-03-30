from clients.authentification.authentification_schema import LoginUserRequestSchema, LoginUserResponsetSchema, CreateUserRequestSchema
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from tools.routes import AppRoute

from requests import Response


class AuthentificationClients(ApiClient):
    def login_user_api(self, request: LoginUserRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.LOGIN_USER, json=request_data)
    
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.CREATE_USER, json=request_data)
    
    def login(self, request: LoginUserRequestSchema) -> LoginUserResponsetSchema:
        response = self.login_user_api(request)
        return LoginUserResponsetSchema.model_validate_json(response.text)
    
def get_authentification_client() -> AuthentificationClients:
    return AuthentificationClients(client=get_public_http_client())