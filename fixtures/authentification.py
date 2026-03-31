from pydantic import BaseModel, EmailStr
from _pytest.fixtures import SubRequest
from typing import Generator
import pytest

from clients.authentification.authentification_client import AuthentificationClients, get_authentification_client
from clients.authentification.authentification_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.private_http_builder import AuthentificationUserSchema
from tools.fakers import fake


class AuthentificationFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email
    
    @property
    def password(self) -> str:
        return self.request.password
    
    @property
    def authentification_user(self) -> AuthentificationUserSchema:
        return AuthentificationUserSchema(email=self.email, password=self.password)

@pytest.fixture
def authentification_client() -> AuthentificationClients:
    return get_authentification_client()

@pytest.fixture
def function_auth(authentification_client: AuthentificationClients) -> Generator[AuthentificationFixture, None, None]:
    request = CreateUserRequestSchema()
    response = authentification_client.create(request=request)
    yield AuthentificationFixture(request=request, response=response)
    authentification_client.delete_user_api(auth=response.access_token)

@pytest.fixture
def function_invalid_params_courier(request: SubRequest, function_auth: AuthentificationFixture):
    case_type = request.param
    cases = {
        "invalid_email": {"email": fake.email(), "password": function_auth.request.password},
        "invalid_password": {"email": function_auth.request.email, "password": fake.password()},
        "invalid_email_and_password": {"email": fake.email(), "password": fake.password()},
    }
    
    return cases[case_type]