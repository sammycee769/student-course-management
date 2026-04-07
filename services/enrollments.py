
from database import enrollments_collections
from models import Role, Enrollment
from schemas import EnrollCourse
from services.courseservice import get_course
from services.userservice import get_user


def enroll_student(request:EnrollCourse):
    __student_validation(request)
    get_course(request.course_title)
    __duplicate_course_validation(request)
    new_enrollment = Enrollment(
        student_username =request.student_username,
        course_title=request.course_title
    )
    enrollments_collections.insert_one(__convert_to_dict(new_enrollment))
    return new_enrollment

def get_student_courses(student_username:str):
    get_user(student_username)
    enrollments= enrollments_collections.find({"student_username": student_username})
    return [__convert_from_dict(enrollment).course_title for enrollment in enrollments]
def get_courses_by_students(course_title:str):
    get_course(course_title)
    enrollments = enrollments_collections.find({"course_title": course_title})
    return [__convert_from_dict(enrollment).student_username for enrollment in enrollments]
def __student_validation(enrollment_request:EnrollCourse):
    student = get_user(str(enrollment_request.student_username))
    if student.role != Role.STUDENT:
        raise Exception('Only students can enroll')

def __duplicate_course_validation(request:EnrollCourse):
    if enrollments_collections.find_one({
        "student_username": request.student_username,
        "course_title": request.course_title
    }):
        raise Exception('Student already enrolled in this course')

def __convert_to_dict(enrollment: Enrollment):
    return {
        "student_username": enrollment.student_username,
        "course_title": enrollment.course_title
    }

def __convert_from_dict(data):
    return Enrollment(
        student_email=data["student_email"],
        course_title=data["course_title"]
    )
