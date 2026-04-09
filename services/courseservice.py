from models.course import Course
from models.role import Role
from schemas import CreateCourse
from services.userservice import get_user
from repositories import course_repository
from exceptions.course_exceptions import (
    CourseNotFoundException,
    CourseAlreadyExistsException,
    UnauthorizedCourseActionException
)


def create_course(request: CreateCourse):
    __validate_role(request)
    __validate_duplicate_course(request)

    new_course = Course(
        title=request.title,
        description=request.description,
        facilitator_username=request.facilitator_username,
    )

    course_repository.save(__convert_to_dict(new_course))
    return new_course


def get_all_courses(username: str):
    get_user(username)

    courses = course_repository.find_all()
    return [__convert_from_dict(course) for course in courses]


def get_courses_by_facilitator(username: str):
    get_user(username)

    courses = course_repository.find_by_facilitator(username)
    return [__convert_from_dict(course) for course in courses]


def get_course(title: str):
    course = course_repository.find_by_title(title)

    if course:
        return __convert_from_dict(course)

    raise CourseNotFoundException("Course not found")


def __validate_duplicate_course(request: CreateCourse):
    if course_repository.find_by_title(request.title):
        raise CourseAlreadyExistsException("Course already exists")


def __validate_role(request: CreateCourse):
    facilitator = get_user(request.facilitator_username)

    if facilitator.role != Role.FACILITATOR:
        raise UnauthorizedCourseActionException(
            "Only facilitators can create courses"
        )


def __convert_to_dict(course: Course):
    return {
        "title": course.title,
        "description": course.description,
        "facilitator_username": course.facilitator_username
    }


def __convert_from_dict(data):
    return Course(
        title=data["title"],
        description=data["description"],
        facilitator_username=data["facilitator_username"]
    )