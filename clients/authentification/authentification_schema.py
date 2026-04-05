from pydantic import BaseModel, ConfigDict, EmailStr, Field

from tools.fakers import fake


class LoginUserRequestSchema(BaseModel):
    email: EmailStr
    password: str

class UserSchema(BaseModel):
    email: EmailStr
    name: str

class LoginUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = Field(default_factory=True)
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")
    user: UserSchema

class LoginUserUnauthorizedResponseSchema(BaseModel):
    success: bool = False
    message: str = "email or password are incorrect"

class CreateUserRequestSchema(BaseModel):
    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    name: str = Field(default_factory=fake.name)

class CreateUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = Field(default_factory=True)
    user: UserSchema
    access_token: str = Field(alias="accessToken")
    refresh_token: str = Field(alias="refreshToken")

class CreateUserDouplicateResponseSchema(BaseModel):
    success: bool = False
    message: str = "User already exists"

class CreateUserRequiredFieldRequestSchema(BaseModel):
    email: str | None
    password: str | None
    name: str | None

class CreateUserRequiredFieldstResponseSchema(BaseModel):
    success: bool = False
    message: str = "Email, password and name are required fields"