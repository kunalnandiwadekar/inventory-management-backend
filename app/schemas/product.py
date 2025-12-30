from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    category: Optional[str] = None
    unit: Optional[str] = None
    price: float
    min_stock: int = 0
    current_stock: int = 0

class ProductOut(ProductCreate):
    id: int

    class Config:
        from_attributes = True
