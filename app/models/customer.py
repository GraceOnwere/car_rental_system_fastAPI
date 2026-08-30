import uuid
from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class Customer(BaseModel):
    __id : UUID = uuid.uuid4()
    __full_name : str = Field(...,min_length=1,max_length=30)
    __email : EmailStr = Field(...,min_length=1,max_length=100)
    __house_address : str = Field(...,min_length=1,max_length=100)
