from database import courses_collection
from models import Role, Course
from schemas import CreateCourse
from services.userservice import get_user

course_db = []

def create_course(request:CreateCourse):
    __validate_role(request)
    __duplicate_course_validation(request)

    new_course = Course(
        title=request.title,
        description=request.description,
        facilitator_username=request.facilitator_username,
    )
    courses_collection.insert_one(__convert_to_dict(new_course))
    return new_course

def get_all_courses(username:str):
    get_user(username)
    courses = courses_collection.find()
    return [__convert_from_dict(course) for course in courses]

def get_courses_by_facilitator(username:str):
    get_user(username)
    courses = courses_collection.find({"facilitator_username": username})
    return [  __convert_from_dict(course) for course in courses  ]

def get_course(title: str):
    course = courses_collection.find_one({"title": title})
    if course :
        return __convert_to_dict(course)
    raise Exception("Course not found")

def __duplicate_course_validation(request:CreateCourse):
    if courses_collection.find_one({ "title": request.title }) :
        raise Exception('Course already exists')
def __validate_role(request:CreateCourse):
    facilitator = get_user(request.facilitator_username)
    if facilitator.role != Role.FACILITATOR:
        raise Exception("Only facilitator can create course")

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