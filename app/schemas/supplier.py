from pydantic import BaseModel

class SupplierCreate(BaseModel):
    name: str
    contact_person: str
    phone: str
    email: str
    address: str


class SupplierOut(BaseModel):
    id: int
    name: str
    contact_person: str
    phone: str
    email: str
    address: str

    class Config:
        orm_mode = True   # ✅ Pydantic v1 (THIS IS THE KEY)
