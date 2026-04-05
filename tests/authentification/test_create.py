from clients.authentification.authentification_client import AuthentificationClients
from clients.authentification.authentification_schema import CreateUserRequestSchema, CreateUserResponseSchema, CreateUserDouplicateResponseSchema, CreateUserRequiredFieldstResponseSchema, CreateUserRequiredFieldRequestSchema
from conftest_helpers.authentification import AuthentificationFixture
from tools.assertions.authentification import assert_create_courier_response, assert_create_courier_without_reqired_fields_response, assert_create_douplicate_courier_response
from tools.assertions.schema import validate_json_schema
from tools.fakers import fake
from tools.assertions.base import assert_status_code

from http import HTTPStatus
import pytest
import allure



class TestCreateUser:
    @allure.title("Create unique user")
    def test_create_unique_user(self, authentification_client: AuthentificationClients):
        request = CreateUserRequestSchema()
        response = authentification_client.create_user_api(request=request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_courier_response(response=response_data, request=request)

        authentification_client.delete_user_api(auth=response_data.access_token)

    @allure.title("Create douplicate user")
    def test_create_douplicate_user(self, function_auth: AuthentificationFixture, authentification_client: AuthentificationClients):
        request = CreateUserRequestSchema(
            email=function_auth.request.email, 
            password=function_auth.request.password, 
            name=function_auth.request.name
            )
        response = authentification_client.create_user_api(request=request)
        response_data = CreateUserDouplicateResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.FORBIDDEN)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_douplicate_courier_response(response=response_data)

    @allure.title("Create without reqired fields user")
    @pytest.mark.parametrize(
        "email, password, name", 
        [
            ("", fake.password(), fake.name()), 
            (fake.email(), "", fake.name()), 
            (fake.email(), fake.password(), "")
            ])
    def test_create_user_without_reqired_fields(self, authentification_client: AuthentificationClients, email, password, name):
        request = CreateUserRequiredFieldRequestSchema(email=email, password=password, name=name)
        response = authentification_client.create_user_api(request=request)
        response_data = CreateUserRequiredFieldstResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.FORBIDDEN)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_courier_without_reqired_fields_response(response=response_data)

