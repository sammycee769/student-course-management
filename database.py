from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

database = client["student_course_management"]

users_collection = database["users"]
courses_collection = database["courses"]
enrollments_collections = database["enrollments"]