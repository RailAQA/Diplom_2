from pydantic import BaseModel
from requests_toolbelt import sessions
from requests import Session

from clients.authentification.authentification_schema import LoginUserRequestSchema
from clients.authentification.authentification_client import get_authentification_client
from tools.routes import AppRoute

class AuthentificationUserSchema(BaseModel):
    """
    Описание структуры запроса на авторизацию юзера
    """
    email: str
    password: str

def get_private_http_client(user: AuthentificationUserSchema) -> Session:
    create_user = get_authentification_client()
    login_request = LoginUserRequestSchema(email=user.email, password=user.password)
    login_response = create_user.login(request=login_request)
    session = sessions.BaseUrlSession(base_url=AppRoute.BASE_URL)
    session.headers.update({"Authorization": login_response.access_token})
    return session