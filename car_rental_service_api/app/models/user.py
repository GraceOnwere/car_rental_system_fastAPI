from abc import ABC

from app.models.role import Role


class User(ABC):
    __username : str = None
    __email : str = None
    __password : str = None
    __role : Role = None