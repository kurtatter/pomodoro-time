import redis

from settings import Settings


settings = Settings()


def get_redis_connection():
    return redis.Redis(
        host=settings.CACHE_HOST,
        port=settings.CACHE_PORT,
        db=settings.CACHE_DB
    )


def set_pomodoro_count(pomodoro_count: int):
    redis_connection = get_redis_connection()
    redis_connection.set('pomodoro_count', pomodoro_count)
