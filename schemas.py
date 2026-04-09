from typing import Optional
from pydantic import BaseModel, Field, EmailStr
from models.role import Role


class RegisterUser(BaseModel):
    username: str = Field(...,min_length=3,max_length=50)
    email: EmailStr
    role:Role


class UpdateUser(BaseModel):
    username: Optional[str] = Field(None,min_length=3,max_length=50)
    email: Optional[EmailStr] = None
    role: Optional[Role] = None


class EnrollCourse(BaseModel):
    course_title: str = Field(...,min_length=5,max_length=50)
    student_username: str = Field(...,min_length=3,max_length=50)


class CreateCourse(BaseModel):
    title: str = Field(...,min_length=1,max_length=50)
    description: str = Field(...,min_length=1,max_length=250)
    facilitator_username: str = Field(...,min_length=3,max_length=50)