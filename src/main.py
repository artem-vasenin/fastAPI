from fastapi import FastAPI
from handlers import routers

app = FastAPI()

for router in routers:
    app.include_router(router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Добро пожаловать в моё приложение FastAPI!"}
