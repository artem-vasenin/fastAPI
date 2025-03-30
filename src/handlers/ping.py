from fastapi import APIRouter

router: APIRouter = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/app")
async def ping_app():
    return {"type": "ping app"}

@router.get("/db")
async def ping_db():
    return {"type": "ping db"}