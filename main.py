from fastapi import FastAPI, HTTPException
from schemas import RegisterUser, UpdateUser, CreateCourse, EnrollCourse
from services.courseservice import create_course, get_all_courses, get_courses_by_facilitator, get_course
from services.enrollments import enroll_student, get_student_courses, get_courses_by_students
from services.userservice import get_user, update_user, delete_user, register_user

app = FastAPI()

@app.post("/users/register")
def register_user_endpoint(request: RegisterUser):
    try:
        return register_user(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users/{username}")
def api_get_user(username: str):
    try:
      return get_user(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.patch("/users/{username}")
def api_update_user(username: str, request: UpdateUser):
    try:
        return update_user(username, request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/users/{username}")
def api_delete_user(username: str):
    try:
        return delete_user(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/courses")
def api_create_course(request: CreateCourse):
    try:
        return create_course(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/all-courses")
def api_get_all_courses(username: str):
    try:
        return get_all_courses(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/courses/facilitator/{username}")
def api_get_courses_by_facilitator(username: str):
    try:
        return get_courses_by_facilitator(username)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/courses/{title}")
def api_get_course(title: str):
    try:
        return get_course(title)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/enrollments")
def api_enroll_student(request: EnrollCourse):
    try:
        return enroll_student(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/enrollments/student/{student_email}")
def api_get_student_courses(student_email: str):
    try:
        return get_student_courses(student_email)
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))

@app.get("/enrollments/course/{course_title}")
def api_get_course_students(course_title: str):
    try:
        return get_courses_by_students(course_title)
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)
