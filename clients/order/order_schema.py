from pydantic import BaseModel, ConfigDict, Field

from tools.fakers import fake


class CreateOrderRequestSchema(BaseModel):
    ingredients: list[str] = Field(default_factory=lambda: [fake.ingrendient()])

class OrderSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    number: int

class CreateOrderWithAuthResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    success: bool = True
    name: str
    order: OrderWithAuthSchema
    
class OrderWithAuthSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    ingredients: list[IngredientsSchema]
    id: str = Field(alias="_id")
    owner: OwnerSchema
    status: str
    name: str
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")
    number: int
    price: int

class IngredientsSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(alias="_id")
    name: str
    type: str
    proteins: int
    fat: int
    carbohydrates: int
    calories: int
    price: int
    image: str
    image_mobile: str
    image_large: str
    v: int = Field(alias="__v")

class OwnerSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    name: str
    email: str
    created_at: str = Field(alias="createdAt")
    updated_at: str = Field(alias="updatedAt")

class CreateOrderWithoutAuthResponseSchema(BaseModel):
    model_config = ConfigDict(extra="forbid")
    
    name: str
    order: OrderSchema
    success: bool = True

class CreateOrderBadRequestResponseSchema(BaseModel):
    success: bool = False
    message: str = Field(default_factory="Ingredient ids must be provided")