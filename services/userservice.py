from database import users_collection
from models import User, Role
from schemas import RegisterUser, UpdateUser

def register_user(request:RegisterUser):
    __validate_duplicate_user(request)
    new_user = User(
        username=request.username,
        email=str(request.email),
        role=request.role
    )
    users_collection.insert_one(__convert_to_dictionary(new_user))
    return new_user

def get_user(username:str):
    user = users_collection.find_one({"username": username})
    if user:
        return __convert_from_dictionary(user)
    raise Exception("User does not exist")

def update_user(username:str,request:UpdateUser):
    user = get_user(username)
    if request.username:
        user.username = request.username
    if request.email:
        user.email = str(request.email)
    if request.role:
        user.role = request.role
    users_collection.update_one(
        {"username": username},
        {"$set": __convert_to_dictionary(user)}
    )
    return user

def delete_user(username:str):
    get_user(username)
    users_collection.delete_one({u"username": username})
    return {"message": f"{username} deleted successfully"}

def __validate_duplicate_user(request: RegisterUser):
    if users_collection.find_one({"username": request.username}):
        raise Exception("Username already exists")
    if users_collection.find_one({"email": request.email}):
        raise Exception("Email already exists")

def __convert_to_dictionary(user: User):
    return {
        "username": user.username,
        "email": user.email,
        "role": user.role.value
    }

def __convert_from_dictionary(data):
    return User(
        username=data["username"],
        email=data["email"],
        role=Role(data["role"])
    )