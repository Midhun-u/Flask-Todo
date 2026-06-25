from schemas.user_schema import Users
from sqlmodel import Session, select
from config.db import engine
from utils.handle_error import handle_error

class UserModel:
    
    def __init__(self):
        pass

    @handle_error
    def add_user(self, fullname: str, email: str, password: str):
   
        user = Users(fullname=fullname, email=email, password=password)

        session = Session(engine)
        with session:
            session.add(user)
            session.commit()
            session.refresh(user)
        
        return user.dict()
    
    @handle_error
    def get_user_by_email(self, email: str): 

        session = Session(engine)

        with session:
            statement = select(Users).where(Users.email == email)
            user = session.execute(statement).scalars().first()

            return user