import streamlit as st
from sqlmodel import SQLModel, create_engine


@st.cache_resource
def connect_to_database():
    engine = create_engine("sqlite:///database.db")  # Create database
    SQLModel.metadata.create_all(engine)  # Create tables
    return engine