from sqlmodel import create_engine, SQLModel
from os import getenv
from schemas.user_schema import Users
from schemas.todo_schema import Todos
from dotenv import load_dotenv

load_dotenv()

database_url = getenv("DATABASE_URL")

if not database_url:
    raise ValueError("Database URL is missing")

engine = create_engine(url=database_url)

def connect_to_database():
    
    try:
        
        SQLModel.metadata.create_all(engine)
        print("Database is connected")

    except Exception as exception:
        print(f"Database is couldn't connect due to {exception}")