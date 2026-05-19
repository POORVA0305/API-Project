from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_name = Column(String)
    age = Column(Integer)
    domain = Column(String)
    marks = Column(Integer)