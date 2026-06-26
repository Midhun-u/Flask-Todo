from sqlmodel import SQLModel, Field
from uuid import uuid4
from datetime import datetime

class Todos(SQLModel, table=True):
    id: str | None = Field(default_factory=uuid4, primary_key=True, allow_mutation=False, nullable=False, unique=True)
    user_id: str = Field(allow_mutation=False, nullable=False, max_length=150, index=True)
    task: str = Field(nullable=False, min_length=5, max_length=100)
    is_completed: bool = Field(default=False, nullable=False)
    created_at: str | None = Field(default_factory=datetime.now().isoformat, nullable=False, allow_mutation=False)