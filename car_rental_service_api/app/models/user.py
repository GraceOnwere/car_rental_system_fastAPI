import uuid
from abc import ABC
from uuid import UUID

from app.models.role import Role


class User(ABC):
    __username : str = None
    __email : str = None
    __password : str = None
    __role : Role = None
    __id: UUID  = uuid.uuid4()