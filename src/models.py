from pydantic import BaseModel


class Account(BaseModel):
    first_name: str
    last_name: str
    email: str = None


class Address(BaseModel):
    name: str
    address: str
    address_extra: str = None
    city_id: str
    postal_code: str
