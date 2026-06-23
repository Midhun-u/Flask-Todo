from schemas.user_schema import Users
from sqlmodel import Session, select
from config.db import engine

class UsersModel:
    
    def __init__(self):
        pass

    def add_user(self, fullname: str, email: str, password: str):
        
        try:
            user = Users(fullname=fullname, email=email, password=password)

            session = Session(engine)
            with session:
                session.add(user)
                session.commit()
                session.refresh(user)
              
            return user.dict()
        except Exception as exception:
            print(exception)

    def get_user_by_email(self, email: str): 

        session = Session(engine)

        with session:

            statement = select(Users).where(Users.email == email)
            results = session.execute(statement)

            for user in results:
                return user[0]

        