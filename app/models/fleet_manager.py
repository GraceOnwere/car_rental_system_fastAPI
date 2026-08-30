from app.models.role import Role
from app.models.user import User

class FleetManager(User):
    __role : Role = Role.FLEET_MANAGER

