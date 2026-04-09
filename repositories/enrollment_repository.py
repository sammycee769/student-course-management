from database import enrollments_collections


def save(enrollment_dict: dict):
    return enrollments_collections.insert_one(enrollment_dict)


def find_by_student(username: str):
    return enrollments_collections.find({
        "student_username": username
    })


def find_by_course(title: str):
    return enrollments_collections.find({
        "course_title": title
    })


def find_one(student_username: str, course_title: str):
    return enrollments_collections.find_one({
        "student_username": student_username,
        "course_title": course_title
    })