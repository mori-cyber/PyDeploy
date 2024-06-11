
import streamlit as st
from sqlmodel import Field, Session, SQLModel, create_engine, select
from models import User, Message  # Assuming these models are defined correctly
from assistant import fetch_response  # A

from Database import connect_to_database

engine = connect_to_database()

def ai(user_text_message):
    ai_text_message = fetch_response(user_text_message)
    return ai_text_message

def message_process(user_text_message:str, username:str, user_id:int):
    # print(username)
    ai_text_message = ai(user_text_message)
    user_message = Message(text=user_text_message, type=username, user_id=user_id)
    ai_message = Message(text=ai_text_message, type="ai", user_id=user_id)
    # print(ai_message)
    # Backend
    with Session(engine) as session:
        session.add(user_message)
        session.add(ai_message)
        session.commit()

    # Frontend
    st.session_state.messages.append({'type': username , 'text': user_text_message})  # In the session_state values are held
    st.session_state.messages.append({'type': 'ai', 'text': ai_text_message})
    
    return ai_text_message


