from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Data Model
class Course(BaseModel):
    id: int
    title: str
    instructor: str
    price: float
    category: str

# Sample Data
courses_db = [
    {"id": 1, "title": "Advanced Python for AI", "instructor": "Dr. Tech", "price": 49.99, "category": "AI/ML"},
    {"id": 2, "title": "Cybersecurity Fundamentals", "instructor": "Ethical Hacker", "price": 39.99, "category": "Security"},
]

@app.get("/")
def read_root():
    return {"message": "Welcome to Cybermind Academy API"}

@app.get("/courses", response_model=List[Course])
def get_courses():
    return courses_db

@app.post("/courses")
def add_course(course: Course):
    courses_db.append(course.dict())
    return {"message": "Course added successfully", "course": course}
