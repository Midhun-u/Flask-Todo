from utils.handle_error import handle_error
from schemas.todo_schema import Todos
from sqlmodel import Session
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