from pydantic import BaseModel, Field, validator
import re

class SupplierCreate(BaseModel):
    name: str
    contact_person: str
    phone: str = Field(..., example="9876543210")
    email: str
    address: str

    @validator("phone")
    def phone_must_be_digits(cls, v):
        if not re.fullmatch(r"\d{10}", v):
            raise ValueError("Phone number must be 10 digits")
        return v


class SupplierOut(BaseModel):
    id: int
    name: str
    contact_person: str
    phone: str
    email: str
    address: str

    class Config:
        from_attributes = True
