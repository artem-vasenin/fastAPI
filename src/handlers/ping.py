from fastapi import APIRouter
from settings import Settings

router: APIRouter = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/app")
async def ping_app():
    settings = Settings()
    return {"type": "ping app", "settings": settings.TOKEN}

@router.get("/db")
async def ping_db():
    return {"type": "ping db"}