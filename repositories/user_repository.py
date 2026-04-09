from database import users_collection


def save(user_dict: dict):
    return users_collection.insert_one(user_dict)


def find_by_username(username: str):
    return users_collection.find_one({"username": username})


def find_by_email(email: str):
    return users_collection.find_one({"email": email})


def update(username: str, updated_user: dict):
    return users_collection.update_one(
        {"username": username},
        {"$set": updated_user}
    )


def delete(username: str):
    return users_collection.delete_one({"username": username})