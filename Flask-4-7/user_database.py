
from sqlmodel import Field , SQLModel, create_engine
from datetime import datetime

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    first_name:str = Field()
    last_name: str = Field()
    email :    str = Field()
    age :      int = Field()
    country :  str = Field()
    join_time: int = Field()
    city:      str = Field()
    username:  str = Field()
    password:  str = Field()
    
class Comment(SQLModel , table = True):
    
    id: int = Field(default=None ,primary_key=True )
    content: str
    timestamp : datetime = Field(default_factory= datetime.now)
    user_id: int = Field(foreign_key="user.id")