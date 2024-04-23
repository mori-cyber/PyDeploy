
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# import psycopg2
import os
from dotenv import load_dotenv
# # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


SQLALCHEMY_DATABASE_URL = load_dotenv(dotenv_path="C:/Users/taban/Videos/liara/app/.env")
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
