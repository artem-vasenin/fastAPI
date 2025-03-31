from pydantic import BaseModel


class Task(BaseModel):
    id: int
    cid: int
    name: str
    cnt: int