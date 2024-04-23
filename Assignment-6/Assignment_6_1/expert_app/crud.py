# CRUD comes from: Create, Read, Update, and Delete
from sqlalchemy.orm import Session
import models , schemas



def get_student(stu_id: int,db:Session):
    return db.query(models.Student).filter(models.Student.id == stu_id).first()

def get_course( course_id: int, db:Session):
    return db.query(models.Course).filter(models.Course.id == course_id).first()


#create student table
def create_student(db:Session, firstname:str,lastname:str,average:float, graduated:bool):
    student_data=models.Student(firstname=firstname,lastname=lastname,average=average, graduated=graduated)
    db.add(student_data)
    db.commit()
    db.refresh(student_data)
    return student_data
#create course table
def create_course(db:Session,name:str,unit:int, owner_id=int ):
    course_data=models.Course(name=name,unit=unit, owner_id=owner_id)
    db.add(course_data)
    db.commit()
    db.refresh(course_data)
    return course_data

def delete_student(student_id, db:Session):
    db.delete(student_id)
    db.commit()
    return {"ok":"this student deleted"}

def delete_course(course_id, db:Session):
    db.delete(course_id)
    db.commit()
    return {"ok":"this course deleted"}

def up_to_date_student( student , firstname: str, lastname: str, average: float, graduated: bool, db: Session):

    student.firstname=firstname
    student.lastname = lastname
    student.average =average
    student.graduate = graduated
    db.commit()
    db.refresh(student)
    return student
def up_to_date_course( course , name:str, unit:int, owner_id: int, db:Session):
    course.owner_id=owner_id
    course.name =name
    course.unit =unit
    db.commit()
    db.refresh(course)
    return course