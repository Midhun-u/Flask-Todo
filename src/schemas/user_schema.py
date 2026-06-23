from sqlmodel import Field, SQLModel
from uuid import uuid4

class Users(SQLModel, table=True):
    id: str | None = Field(default=uuid4(), primary_key=True, allow_mutation=False, nullable=False, unique=True)
    fullname: str = Field(default=None, nullable=False, min_length=3, max_length=30)
    email: str = Field(default=None, nullable=False, unique=True, max_length=300, regex=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    password: str = Field(default=None, nullable=False, min_length=6, max_length=300)