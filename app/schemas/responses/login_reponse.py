from pydantic import BaseModel

class LoginUserResponse(BaseModel):
    username: str
    logged_in: bool
