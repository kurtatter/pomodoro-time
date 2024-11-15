from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    GOOGLE_TOKEN_ID: str = "6dcd4ce23d88e2ee9568ba546c007c63d4f1c3b0c1c1c1c1c1c1c1c1c1c1c1c1"
    db_url: str = 'postgresql+psycopg2://postgres:password@localhost:5432/pomodoro'
