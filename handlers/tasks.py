from typing import Annotated

from fastapi import APIRouter, status, Depends

from dependency import get_tasks_db_repository, get_task_service
from schema.task import TaskSchema
from repository import TaskDBRepository
from service.task import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/{task_id}", response_model=TaskSchema)
async def get_task(
        task_id: int,
        task_db_repository: Annotated[TaskDBRepository, Depends(get_tasks_db_repository)]
):
    return task_db_repository.get_task(task_id)


@router.get("/", response_model=list[TaskSchema])
async def get_all_tasks(
        task_service: Annotated[TaskService, Depends(get_task_service)]
):
    return task_service.get_tasks()


@router.post("/", response_model=TaskSchema)
async def create_task(
        task: TaskSchema,
        task_db_repository: Annotated[TaskDBRepository, Depends(get_tasks_db_repository)]
):
    task_id = task_db_repository.create_task(task)
    task.id = task_id
    return task


@router.patch("/{task_id}", response_model=TaskSchema)
async def patch_task(
        task_id: int,
        name: str,
        task_db_repository: Annotated[TaskDBRepository, Depends(get_tasks_db_repository)]
):
    return task_db_repository.update_task_name(task_id, name)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
        task_id: int,
        task_db_repository: Annotated[TaskDBRepository, Depends(get_tasks_db_repository)]
):
    task_db_repository.delete_task(task_id)

    return {"message": "task deleted"}
