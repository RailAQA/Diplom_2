from tools.assertions.base import assert_equal, assert_is_true
from clients.order.order_schema import CreateOrderResponseSchema, CreateOrderBadRequestResponseSchema


def assert_create_order_response(response: CreateOrderResponseSchema):
    assert_is_true(actual=response.name, name="name")
    assert_is_true(actual=response.order.number, name="order_number")
    assert_equal(actual=response.success, expected=True, name="success")

def assert_create_order_without_ingrendients_response(response: CreateOrderBadRequestResponseSchema):
    assert_equal(actual=response.success, expected=False, name="success")
    assert_equal(actual=response.message, expected="Ingredient ids must be provided", name="message")