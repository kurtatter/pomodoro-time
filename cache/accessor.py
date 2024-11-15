import redis


def get_redis_connection():
    return redis.Redis(
        host='localhost',
        port=6379,
        db=0
    )


def set_pomodoro_count(pomodoro_count: int):
    redis_connection = get_redis_connection()
    redis_connection.set('pomodoro_count', pomodoro_count)
