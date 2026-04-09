from pydantic import BaseModel


class Grade(BaseModel):
    student_email: str
    course_title: str
    grade: str
    facilitator_email: str