from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db_session
from cache import get_redis_connection
from repository import TaskDBRepository, TaskCacheRepository, UserRepository
from service import TaskService, UserService


def get_tasks_db_repository(db_session: Session = Depends(get_db_session)) -> TaskDBRepository:
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


def get_user_repository(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repository=user_repository)
