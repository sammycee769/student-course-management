from database import courses_collection


def save(course_dict: dict):
    return courses_collection.insert_one(course_dict)


def find_all():
    return courses_collection.find()


def find_by_title(title: str):
    return courses_collection.find_one({"title": title})


def find_by_facilitator(username: str):
    return courses_collection.find({
        "facilitator_username": username
    })


def delete(title: str):
    return courses_collection.delete_one({"title": title})