# from pydantic import BaseModel


# class CourseBase(BaseModel):
#     id:int
#     name:str
#     unit:int

# class CourseCreate(CourseBase):
#     id=int
#     name=str
#     unit=int

# class Course(CourseBase):
#     id: int
#     name=str
#     unit=int

#     class Config:
#         orm_mode = True


# class StudentBase(BaseModel):
#     id:int
#     firstname:str
#     lastname: str
#     average:float
#     graduated:bool


# class StudentCreate(StudentBase):
#     id:int
#     firstname:str
#     lastname: str
#     average:float
#     graduated:bool



# class Student(StudentBase):
#     id: int
#     firstname:str
#     lastname: str
#     average:float
#     graduated:bool
#     is_active: bool
#     items: list[Course] = []

#     class Config:
#         orm_mode = True