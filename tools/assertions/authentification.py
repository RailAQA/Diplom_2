from clients.authentification.authentification_schema import CreateUserResponseSchema, CreateUserRequestSchema, CreateUserDouplicateResponseSchema, CreateUserRequiredFieldstResponseSchema, LoginUserResponseSchema, LoginUserRequestSchema, LoginUserUnauthorizedResponseSchema
from tools.assertions.base import assert_equal, assert_is_true


def assert_create_courier_response(response: CreateUserResponseSchema, request: CreateUserRequestSchema):
    assert_equal(actual=response.success, expected=True, name="success")
    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_equal(actual=response.user.name, expected=request.name, name="name")
    assert_is_true(actual=response.access_token, name="access_token")
    assert_is_true(actual=response.refresh_token, name="refresh_token")

def assert_create_douplicate_courier_response(response: CreateUserDouplicateResponseSchema):
    assert_equal(actual=response.success, expected=False, name="success")
    assert_equal(actual=response.message, expected="User already exists", name="message")

def assert_create_courier_without_reqired_fields_response(response: CreateUserRequiredFieldstResponseSchema):
    assert_equal(actual=response.success, expected=False, name="success")
    assert_equal(actual=response.message, expected="Email, password and name are required fields", name="message")

def assert_login_response(response: LoginUserResponseSchema, request: LoginUserRequestSchema):
    assert_equal(actual=response.success, expected=True, name="success")
    assert_equal(actual=response.user.email, expected=request.email, name="email")
    assert_is_true(actual=response.user.name, name="name")
    assert_is_true(actual=response.access_token, name="access_token")
    assert_is_true(actual=response.refresh_token, name="refresh_token")

def assert_login_with_invalid_params_response(response: LoginUserUnauthorizedResponseSchema):
    assert_equal(actual=response.success, expected=False, name="success")
    assert_equal(actual=response.message, expected="email or password are incorrect", name="message")