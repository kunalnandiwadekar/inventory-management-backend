from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    category: str
    unit: str
    price: float
    min_stock: int
    current_stock: int


class ProductOut(BaseModel):
    id: int                      
    name: str
    category: str
    unit: str
    price: float
    min_stock: int
    current_stock: int

    class Config:
        orm_mode = True
