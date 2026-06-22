from sqlmodel import create_engine, SQLModel
from os import getenv

def connect_to_database():
    
    try:
        database_url = getenv("DATABASE_URL")
        engine = create_engine(url=database_url, echo=True)

        SQLModel.metadata.create_all(engine)
    except Exception as exception:
        print(f"Database is couldn't connect due to {exception}")