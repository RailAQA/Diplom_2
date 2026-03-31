from clients.authentification.authentification_schema import LoginUserRequestSchema, LoginUserResponseSchema, CreateUserRequestSchema, CreateUserResponseSchema
from clients.api_client import ApiClient
from clients.public_http_builder import get_public_http_client
from tools.routes import AppRoute

from requests import Response
import allure


class AuthentificationClients(ApiClient):
    @allure.step("Login user")
    def login_user_api(self, request: LoginUserRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.LOGIN_USER, json=request_data)
    
    @allure.step("Create user")
    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        request_data = request.model_dump(by_alias=True)
        return self.post(url=AppRoute.CREATE_USER, json=request_data)
    
    @allure.step("Delete user")
    def delete_user_api(self, auth) -> Response:
        return self.delete(url=AppRoute.DELETE_USER, auth=auth)
    
    @allure.step("Login user")
    def login(self, request: LoginUserRequestSchema) -> LoginUserResponseSchema:
        response = self.login_user_api(request)
        return LoginUserResponseSchema.model_validate_json(response.text)
    
    @allure.step("Create user")
    def create(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)
    
def get_authentification_client() -> AuthentificationClients:
    return AuthentificationClients(client=get_public_http_client())