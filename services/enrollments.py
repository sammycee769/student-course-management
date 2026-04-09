from models.enrollment import Enrollment
from models.role import Role
from schemas import EnrollCourse
from services.courseservice import get_course
from services.userservice import get_user
from repositories import enrollment_repository
from exceptions.enrollment_exceptions import (
    EnrollmentAlreadyExistsException,
    UnauthorizedEnrollmentException
)


def enroll_student(request: EnrollCourse):
    __validate_student(request)
    get_course(request.course_title)
    __validate_duplicate(request)

    new_enrollment = Enrollment(
        student_username=request.student_username,
        course_title=request.course_title
    )

    enrollment_repository.save(__convert_to_dict(new_enrollment))
    return new_enrollment


def get_student_courses(student_username: str):
    get_user(student_username)

    enrollments = enrollment_repository.find_by_student(student_username)
    return [
        __convert_from_dict(enrollment).course_title
        for enrollment in enrollments
    ]


def get_courses_by_students(course_title: str):
    get_course(course_title)

    enrollments = enrollment_repository.find_by_course(course_title)
    return [
        __convert_from_dict(enrollment).student_username
        for enrollment in enrollments
    ]



def __validate_student(request: EnrollCourse):
    student = get_user(request.student_username)

    if student.role != Role.STUDENT:
        raise UnauthorizedEnrollmentException(
            "Only students can enroll"
        )


def __validate_duplicate(request: EnrollCourse):
    if enrollment_repository.find_one(
        request.student_username,
        request.course_title
    ):
        raise EnrollmentAlreadyExistsException(
            "Student already enrolled in this course"
        )



def __convert_to_dict(enrollment: Enrollment):
    return {
        "student_username": enrollment.student_username,
        "course_title": enrollment.course_title
    }


def __convert_from_dict(data):
    return Enrollment(
        student_username=data["student_username"],  # ✅ FIXED
        course_title=data["course_title"]
    )