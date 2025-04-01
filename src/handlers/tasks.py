from fastapi import APIRouter

from src.mocks import tasks, cats
from src.schemas.task import Task

router: APIRouter = APIRouter(prefix="/tasks", tags=["tasks"])

def get_by_id(idx: int) -> Task:
    lst = [i for i in tasks if i["id"] == idx]
    return lst[0] if len(lst) > 0 else None


@router.get("/", response_model=list[Task], status_code=200)
async def get_list():
    return tasks


@router.get("/{tid}", response_model=Task, status_code=200)
async def get_item(tid: int):
    return get_by_id(tid)


@router.delete("/{tid}", response_model=Task|None)
async def remove(tid: int):
    task = get_by_id(tid)
    if not task:
        return None

    lst = [idx for idx, i in enumerate(tasks) if i["id"] == tid]
    if len(lst):
        del tasks[lst[0]]

    return task


@router.post("/", response_model=Task, status_code=201)
async def create(data: Task):
    tasks.append(data)
    return data


@router.put("/{tid}", response_model=Task, status_code=200)
async def update(tid: int, name: str):
    task = get_by_id(tid)
    if task:
        task['name'] = name
    return task