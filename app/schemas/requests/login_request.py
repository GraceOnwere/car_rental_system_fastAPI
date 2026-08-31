from typing import Optional

from pydantic import BaseModel, Field, EmailStr

class LoginUserRequest(BaseModel):
    username : str = Field(...,min_length=1,max_length=20)
    password : str = Field(...,min_length=8,max_length=20)
    email: Optional[EmailStr] = Field(default=None,min_length=8,max_length=20)
