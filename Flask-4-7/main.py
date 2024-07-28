from user_database import User
from fastapi import FastAPI
from sqlmodel import Session, select
from app import engine

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"this is my api"}


@app.get("/register_users")
def get_all_users():
    users_list = []
    with Session(engine) as db_session:
        user = select(User)
        users = db_session.exec(user).all()
        for user in users:
            users_list.append([user.id])
        return len(users_list)
    
@app.get("/admin_info")
def admin_information():
    
    return {    "name":"morteza",
                "last_name":"dehghani",
                "field_of_edu":"AI",
                "country":"Iran"        
    }