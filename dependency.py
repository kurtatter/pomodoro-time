from fastapi import Depends

from database import get_db_session
from cache import get_redis_connection
from repository import TaskDBRepository, TaskCacheRepository
from service import TaskService


def get_tasks_db_repository() -> TaskDBRepository:
    db_session = get_db_session()
    return TaskDBRepository(db_session)


def get_tasks_cache_repository() -> TaskCacheRepository:
    redis_connection = get_redis_connection()
    return TaskCacheRepository(redis_connection)


def get_task_service(
        task_db_repository: TaskDBRepository = Depends(get_tasks_db_repository),
        task_cache_repository: TaskCacheRepository = Depends(get_tasks_cache_repository)

) -> TaskService:
    return TaskService(
        task_db_repository=task_db_repository,
        task_cache_repository=task_cache_repository)
