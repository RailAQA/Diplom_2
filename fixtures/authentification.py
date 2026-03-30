from pydantic import BaseModel, EmailStr
import pytest

from clients.authentification.authentification_client import AuthentificationClients, get_authentification_client
from clients.authentification.authentification_schema import CreateUserRequestSchema, CreateUserResponseSchema
from clients.private_http_builder import AuthentificationUserSchema


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
def function_auth(authentification_client: AuthentificationClients) -> AuthentificationFixture:
    request = CreateUserRequestSchema()
    response = authentification_client.create(request=request)
    return AuthentificationFixture(request=request, response=response)