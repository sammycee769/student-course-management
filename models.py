from enum import Enum
from pydantic import BaseModel


class Role(str, Enum):
    STUDENT = "student"
    FACILITATOR = "facilitator"


# class CourseTitle(str, Enum):
#     MATHS = "Math"
#     ENGLISH = "English"
#     PHYSICS = "Physics"
#     CHEMISTRY = "Chemistry"
#     BIOLOGY = "Biology"
#     GEOGRAPHY = "Geography"


class User(BaseModel):
    username: str
    email: str
    role: Role


class Course(BaseModel):
    title: str
    description:str
    facilitator_username: str


class Enrollment(BaseModel):
    student_email: str
    course_title: str

class Grade(BaseModel):
    student_email: str
    course_title: str
    grade: str
    facilitator_email: str

