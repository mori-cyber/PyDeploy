import streamlit as st
from sqlmodel import  Session
from models import User
from Database import connect_to_database

engine = connect_to_database()

def user_process(name: str, email: str, username: str, password: str):
    user_info = User(name=name, email=email, username=username, password=password)
    with Session(engine) as session:
        session.add(user_info)
        session.commit()


