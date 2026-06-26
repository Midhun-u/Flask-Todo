from utils.handle_error import handle_error
from schemas.todo_schema import Todos
from sqlmodel import Session, select, desc
from config.db import engine
from schemas.todo_schema import Todos

class TodoModel(): 
    
    def __init__(self): 
        pass

    @handle_error
    def add_todo(self, task: str, user_id: str) -> dict[str, any] | None: 
       
        todo = Todos(task=task, user_id=user_id)
        session = Session(engine)

        with session:
            session.add(todo)
            session.commit()
            session.refresh(todo)

        return todo.dict()

    @handle_error
    def get_user_todos(self, user_id: str, page: int, limit: int):
        
        session = Session(engine)
        statement = select(Todos).where(Todos.user_id == user_id).offset((page - 1) * limit).limit(limit)

        with session:
            results = session.execute(statement=statement).scalars().all()
            todos = [result.dict() for result in results]
            return todos

    @handle_error
    def get_todo_by_id_and_user_id(self, id: str, user_id: str):
        
        session = Session(engine)
        statement = select(Todos).where(Todos.id == id and Todos.user_id == user_id)

        with session:
            todo = session.execute(statement=statement).scalars().first()
            return todo.dict()
