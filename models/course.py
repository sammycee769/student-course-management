from pydantic import BaseModel


class Course(BaseModel):
    title: str
    description:str
    facilitator_username: str