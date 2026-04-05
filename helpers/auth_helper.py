from pydantic import BaseModel, EmailStr
from contextlib import contextmanager

from clients.authentification.authentification_client import AuthentificationClients
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
    
@contextmanager
def create_user_context(client: AuthentificationClients):
    """Контекстный менеджер для создания и автоматического удаления пользователя"""
    request = CreateUserRequestSchema()
    response = client.create(request=request)
    user = AuthentificationFixture(request=request, response=response)
    try:
        yield user
    finally:
        client.delete_user_api(auth=response.access_token)