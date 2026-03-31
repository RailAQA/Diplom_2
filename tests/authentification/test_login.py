from http import HTTPStatus
import pytest
import allure

from clients.authentification.authentification_schema import LoginUserRequestSchema, LoginUserResponseSchema, LoginUserUnauthorizedResponseSchema
from clients.authentification.authentification_client import AuthentificationClients
from fixtures.authentification import AuthentificationFixture
from tools.assertions.authentification import assert_login_response, assert_login_with_invalid_params_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema


class TestLogin:
    @allure.title("Successful login")
    def test_successful_login(self, function_auth: AuthentificationFixture, authentification_client: AuthentificationClients):
        request = LoginUserRequestSchema(
            email=function_auth.request.email, 
            password=function_auth.request.password
            )
        response = authentification_client.login_user_api(request=request)
        response_data = LoginUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_login_response(response=response_data, request=request)


    @allure.title("Login with invalid email or password")
    @pytest.mark.parametrize("function_invalid_params_courier",
                             [
                                 "invalid_email",
                                 "invalid_password",
                                 "invalid_email_and_password"
                             ], indirect=True)
    def test_login_with_invalid_email_or_password(self, authentification_client: AuthentificationClients, function_invalid_params_courier):
        request = LoginUserRequestSchema(
            email=function_invalid_params_courier["email"], 
            password=function_invalid_params_courier["password"]
            )
        response = authentification_client.login_user_api(request=request)
        response_data = LoginUserUnauthorizedResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNAUTHORIZED)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_login_with_invalid_params_response(response=response_data)