from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    id: int
    content: str

msg_db: list[Msg] = [Msg(id=0, content='Hello Rusich')]

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
async def add_msg(msg: Msg)->list[Msg]:
    if any(m.id == msg.id for m in msg_db):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Msg already exist')
    msg_db.append(msg)
    return msg_db

@app.put('/msg/{idx}', response_model=Msg)
async def update_msg(msg: Msg, idx: int)->Msg:
    if msg.id != idx:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="id is not eq")
    for i, m in enumerate(msg_db):
        if m.id == idx:
            msg_db[i] = msg
            return msg
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Msg not found")

@app.delete('/msg/{idx}')
async def del_msg(idx: int)->list[Msg]:
    for i, m in enumerate(msg_db):
        if m.id == idx:
            del msg_db[i]
            return msg_db
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Msg not found")
