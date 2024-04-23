from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import crud, models, schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/student/")
def create_student(  firstname:str , lastname:str, average:float, graduated:bool, db: Session = Depends(get_db) ):
    db_student = crud.create_student(db, firstname=firstname, lastname = lastname, average = average, graduated=graduated)
    # if db_student:
    #     raise HTTPException(status_code=400, detail="student already registered")
    return db_student

@app.post("/course/")
def create_course(name:str, unit:int, owner_id:int, db: Session = Depends(get_db)):
    db_course = crud.create_course(db, name=name, unit= unit, owner_id =owner_id)
    # if db_course:
    #     raise HTTPException(status_code=400, detail="course already registered")
    return db_course


@app.get("/student/{student_id}")
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="student not found")
    return db_student


@app.get("/course/{course_id}")
def read_course(course_id: int, db: Session = Depends(get_db)):
    db_course = crud.get_course(db, course_id=course_id)
    if db_course is None:
        raise HTTPException(status_code=404, detail="course not found")
    return db_course

@app.delete("/students/{id}")
def remove_student(id:int,db:Session=Depends(get_db)):
    student=crud.get_student(id,db)
    if student is None:
        raise HTTPException(status_code=404,detail="student not found")    
    return crud.delete_student(student,db)

@app.delete("/courses/{id}")
def remove_course(id:int,db:Session=Depends(get_db)):
    course=crud.get_course(id,db)
    if course is None:
        raise HTTPException(status_code=404,detail="course not found")    
    return crud.delete_course(course,db)


@app.put("/students/{id}")
def update_student(student_id:int,firstname:str,lastname:str,average:float,graduated:bool,db:Session=Depends(get_db)):
    student=crud.get_student(student_id,db)
    if student is None:
        raise HTTPException(status_code=404,detail="student not found")    
    return crud.up_to_date_student(student,firstname,lastname,average,graduated,db)


@app.put("/courses/{id}")
def update_course(id:int,name:str,unit:int,owner_id:int,db:Session=Depends(get_db)):
    course=crud.get_course(id,db)
    if course is None:
        raise HTTPException(status_code=404,detail="course not found")    
    return crud.up_to_date_course(course,name,unit,owner_id,db)