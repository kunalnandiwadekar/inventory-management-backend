from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    category: str
    unit: str
    price: float
    min_stock: int
    current_stock: int


class ProductCreate(BaseModel):
    name: str
    category: str
    unit: str
    price: float
    min_stock: int
    current_stock: int


    class Config:
        orm_mode = True

