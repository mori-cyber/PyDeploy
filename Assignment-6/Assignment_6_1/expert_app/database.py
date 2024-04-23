
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
import os
from dotenv import load_dotenv
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
load_dotenv(dotenv_path="/home/morteza/Desktop/my_python_project/FastAPI/class_work_7/expert_app/.env")

SQLALCHEMY_DATABASE_URL = os.environ.get("PASSWORD")


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
