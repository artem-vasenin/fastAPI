from datetime import datetime

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    cid: int | None = None
    name: str
    cnt: int
    created_at: datetime = Field(exclude=True)