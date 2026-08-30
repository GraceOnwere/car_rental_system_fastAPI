import uuid
from abc import ABC
from typing import Optional
from uuid import UUID

from pydantic import BaseModel ,Field as PydanticField
from sqlmodel import SQLModel ,Field as SQLModelField

from app.models.role import Role

class RegisterUserRequest(BaseModel):
    username : str = PydanticField(...,min_length=1,max_length=20)
    email : str = PydanticField(...,min_length=9,max_length=20)
    password : str = PydanticField(...,min_length=8,max_length=20)
    full_name : str = PydanticField(...,min_length=1,max_length=20)
    role : Role = PydanticField(...,min_length=1,max_length=20)

class RegisterUserResponse(BaseModel):
    user_id : Optional[int] = None
    username : str = None
    email : str = None
    role : Role = None
    message : Optional[str] = None

class UpdateUserRequest(BaseModel):
    username : Optional[str] = None
    email : Optional[str] = None
    full_name : Optional[str] = None
    password : Optional[str] = None

class LoginUserRequest(BaseModel):
    username : str = PydanticField(...,min_length=1,max_length=20)
    password : str = PydanticField(...,min_length=8,max_length=20)

class LoginUserResponse(BaseModel):
    message : str = None

class User(ABC,SQLModel,table=True):
    id: UUID = SQLModelField(default_factory=uuid.uuid4,primary_key=True)
    full_name : str
    username : str = SQLModelField(unique=True)
    email : str = SQLModelField(unique=True)
    password : str
    role : Role
    is_logged_in: bool = False
