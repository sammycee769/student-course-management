from pydantic import BaseModel


class Enrollment(BaseModel):
    student_username: str
    course_title: str