from pydantic import BaseModel
from sqlmodel import Field

class RegisterModel(BaseModel):
    first_name:str 
    last_name: str
    email :    str
    age :      int 
    country :  str 
    join_time: int 
    city:      str
    username:  str
    password:  str
    confirm_password: str
      
class LoginModel(BaseModel):
    username: str
    password: str
    confirm_password: str