from app.models import role
from app.models.role import Role
from app.models.user import User


class FrontDesk(User):
    __role : Role = Role.FRONT_DESK