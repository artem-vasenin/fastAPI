from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
import time

app = FastAPI()

class Msg(BaseModel):
    id: int
    content: str

class CreateMsg(BaseModel):
    content: str

msg_db: list[Msg] = [Msg(id=1, content='Hello Rusich')]

@app.get('/msg', response_model=list[Msg])
async def get_list()->list[Msg]:
    return msg_db

@app.get('/msg/{idx}', response_model=Msg)
async def get_item(idx: int)->Msg:
    for m in msg_db:
        if m.id == idx:
            return m
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item is not found')

@app.post('/msg', response_model=list[Msg], status_code=status.HTTP_201_CREATED)
async def add_msg(msg: CreateMsg)->list[Msg]:
    ts_ms = int(time.time() * 1000)
    msg_db.append(Msg(id=ts_ms, content=msg.content))
    return msg_db

@app.put('/msg/{idx}', response_model=list[Msg])
async def update_msg(msg: CreateMsg, idx: int)->list[Msg]:
    for i, m in enumerate(msg_db):
        if m.id == idx:
            msg_db[i].content = msg.content
            return msg_db
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Msg not found")

@app.delete('/msg/{idx}')
async def del_msg(idx: int)->list[Msg]:
    for i, m in enumerate(msg_db):
        if m.id == idx:
            del msg_db[i]
            return msg_db
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Msg not found")
