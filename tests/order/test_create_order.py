from http import HTTPStatus
import pytest
import allure

from clients.order.order_schema import CreateOrderRequestSchema, CreateOrderBadRequestResponseSchema, CreateOrderResponseSchema
from clients.order.order_client import OrderClients
from tools.assertions.base import assert_status_code
from tools.assertions.order import assert_create_order_with_auth_response, assert_create_order_without_ingrendients_response
from tools.assertions.schema import validate_json_schema


class TestOrder:
    @allure.title("Successful create order with auth")
    def test_create_order_with_auth(self, order_client: OrderClients):
        request = CreateOrderRequestSchema()
        response = order_client.create_order_api(request=request)
        response_data = CreateOrderResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_order_with_auth_response(response=response_data)

    @allure.title("Create order without ingredients")
    def test_create_order_without_ingrendients(self, order_client: OrderClients):
        request = CreateOrderRequestSchema(ingredients=[])
        response = order_client.create_order_api(request=request)
        response_data = CreateOrderBadRequestResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_order_without_ingrendients_response(response=response_data)

    @allure.title("Create order with invalid ingredients")
    def test_create_order_with_bad_ingrendients(self, order_client: OrderClients):
        request = CreateOrderRequestSchema(ingredients=["fake"])
        response = order_client.create_order_api(request=request)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.INTERNAL_SERVER_ERROR)
    
    @allure.title("Create order without auth")
    def test_create_order_without_auth(self, public_order_client: OrderClients):
        request = CreateOrderRequestSchema()
        response = public_order_client.create_order_api(request=request)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
