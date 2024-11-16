from dataclasses import dataclass

from repository import TaskDBRepository, TaskCacheRepository
from schema import TaskSchema


@dataclass
class TaskService:
    task_db_repository: TaskDBRepository
    task_cache_repository: TaskCacheRepository

    def get_tasks(self) -> list[TaskSchema]:
        if cache_tasks := self.task_cache_repository.get_tasks():
            return cache_tasks
        else:
            tasks_from_db = self.task_db_repository.get_tasks()
            tasks_schema = [TaskSchema.model_validate(task) for task in tasks_from_db]
            self.task_cache_repository.set_tasks(tasks_schema)
        return tasks_schema
