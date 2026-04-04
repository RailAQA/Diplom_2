from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class CreateOrderRequestSchema(BaseModel):
    ingredients: list[str] = Field(default_factory=lambda: [fake.ingrendient()])

class OrderSchema(BaseModel):
    number: int

class CreateOrderResponseSchema(BaseModel):
    name: str
    order: OrderSchema
    success: bool = True

class CreateOrderBadRequestResponseSchema(BaseModel):
    success: bool = False
    message: str = Field(default_factory="Ingredient ids must be provided")