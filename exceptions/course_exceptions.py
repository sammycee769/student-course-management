class CourseNotFoundException(Exception):
    pass


class CourseAlreadyExistsException(Exception):
    pass


class UnauthorizedCourseActionException(Exception):
    pass