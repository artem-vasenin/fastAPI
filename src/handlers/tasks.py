from fastapi import APIRouter

router: APIRouter = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/list")
async def get_list():
    return {"type": "tasks list"}

@router.post("/")
async def create():
    return {"type": "create task"}