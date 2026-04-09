from pydantic import BaseModel

from models.role import Role


class User(BaseModel):
    username: str
    email: str
    role: Role
