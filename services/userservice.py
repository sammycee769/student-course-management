from models.role import Role
from models.user import User
from schemas import RegisterUser, UpdateUser
from repositories import user_repository
from exceptions.user_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException
)


def register_user(request: RegisterUser):
    __validate_duplicate_user(request)

    new_user = User(
        username=request.username,
        email=str(request.email),
        role=request.role
    )

    user_repository.save(__convert_to_dictionary(new_user))
    return new_user


def get_user(username: str):
    user = user_repository.find_by_username(username)

    if user:
        return __convert_from_dictionary(user)

    raise UserNotFoundException("User does not exist")


def update_user(username: str, request: UpdateUser):
    user = get_user(username)

    if request.username:
        user.username = request.username

    if request.email:
        user.email = str(request.email)

    if request.role:
        user.role = request.role

    user_repository.update(username, __convert_to_dictionary(user))
    return user


def delete_user(username: str):
    get_user(username)
    user_repository.delete(username)

    return {"message": f"{username} deleted successfully"}


def __validate_duplicate_user(request: RegisterUser):
    if user_repository.find_by_username(request.username):
        raise UserAlreadyExistsException("Username already exists")

    if user_repository.find_by_email(str(request.email)):
        raise UserAlreadyExistsException("Email already exists")


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