from tools.assertions.base import assert_equal, assert_is_true
from clients.order.order_schema import CreateOrderBadRequestResponseSchema, CreateOrderWithoutAuthResponseSchema, CreateOrderWithAuthResponseSchema


def assert_create_order_with_auth_response(response: CreateOrderWithAuthResponseSchema):
    assert_equal(actual=response.success, expected=True, name="success")
    assert_is_true(actual=response.name, name="name")
    assert_is_true(actual=response.order.ingredients, name="ingredients")
    assert_is_true(actual=response.order.id, name="id")
    assert_is_true(actual=response.order.owner.name, name="owner_name")
    assert_is_true(actual=response.order.owner.email, name="owner_email")
    assert_is_true(actual=response.order.owner.created_at, name="owner_created_at")
    assert_is_true(actual=response.order.owner.updated_at, name="owner_updated_at")
    assert_is_true(actual=response.order.status, name="order_status")
    assert_is_true(actual=response.order.name, name="order_name")
    assert_is_true(actual=response.order.created_at, name="order_created_at")
    assert_is_true(actual=response.order.updated_at, name="order_updated_at")
    assert_is_true(actual=response.order.number, name="order_number")
    assert_is_true(actual=response.order.price, name="order_price")

def assert_create_order_without_auth_response(response: CreateOrderWithoutAuthResponseSchema):
    assert_is_true(actual=response.name, name="name")
    assert_is_true(actual=response.order.number, name="order_number")
    assert_equal(actual=response.success, expected=True, name="success")

def assert_create_order_without_ingrendients_response(response: CreateOrderBadRequestResponseSchema):
    assert_equal(actual=response.success, expected=False, name="success")
    assert_equal(actual=response.message, expected="Ingredient ids must be provided", name="message")