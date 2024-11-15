from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("/settings")
def get_settings():
    from settings import Settings
    settings = Settings()
    return settings
