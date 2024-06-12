from sqlmodel import SQLModel, create_engine




engine = create_engine("sqlite:///database.db")  # Create database
SQLModel.metadata.create_all(engine)  # Create tables
