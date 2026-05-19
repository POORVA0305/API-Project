from pydantic import BaseModel

class StudentCreate(BaseModel):
    student_name: str
    age: int
    domain: str
    marks: int

class StudentResponse(StudentCreate):
    id: int

    class Config:
        from_attributes = True
