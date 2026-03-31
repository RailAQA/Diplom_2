from http import HTTPStatus
import pytest

from clients.order.order_schema import CreateOrderRequestSchema, CreateOrderResponseSchema, CreateOrderBadRequestResponseSchema
from clients.order.order_client import OrderClients
from tools.assertions.base import assert_status_code
from tools.assertions.order import assert_create_order_response, assert_create_order_without_ingrendients_response
from tools.assertions.schema import validate_json_schema


class TestOrder:
    def test_create_order(self, order_client: OrderClients):
        request = CreateOrderRequestSchema()
        response = order_client.create_order_api(request=request)
        response_data = CreateOrderResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_order_response(response=response_data)

    def test_create_order_without_ingrendients(self, order_client: OrderClients):
        request = CreateOrderRequestSchema(ingredients=[])
        response = order_client.create_order_api(request=request)
        response_data = CreateOrderBadRequestResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.BAD_REQUEST)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())
        assert_create_order_without_ingrendients_response(response=response_data)

    @pytest.mark.test
    def test_create_order_with_bad_ingrendients(self, order_client: OrderClients):
        request = CreateOrderRequestSchema(ingredients=["fake"])
        response = order_client.create_order_api(request=request)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.INTERNAL_SERVER_ERROR)
