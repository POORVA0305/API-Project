from sqlalchemy.orm import Session
import models
import schemas


def create_student(db: Session, student: schemas.StudentCreate):

    db_student = models.Student(
        student_name=student.student_name,
        age=student.age,
        domain=student.domain,
        marks=student.marks
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


def get_students(db: Session):
    return db.query(models.Student).all()

def delete_student(db: Session, student_id: int):

    student = db.query(models.Student).filter(
        models.Student.id == student_id
    ).first()

    if student:
        db.delete(student)
        db.commit()
        return {"message": "Student deleted successfully"}

    return {"message": "Student not found"}