from sqlmodel import  Session
from models import User
from sqlmodel import SQLModel, create_engine, select

engine = create_engine("sqlite:///database.db")  # Create database
SQLModel.metadata.create_all(engine)  # Create tables


def register( email: str, password: str):
    user_info = User(email=email, password=password)
    with Session(engine) as session:
        session.add(user_info)
        session.commit()

def auth(email , password):
    with Session(engine) as session:
            result = select(User).where(User.email == email and User.password== password)
            user = session.exec(result).first()  
            if user:
                return True
                                        
            else:
               
                return False
            