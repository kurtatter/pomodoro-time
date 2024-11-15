from dataclasses import dataclass

from schema import UserLoginSchema


@dataclass
class UserService:
    def __init__(self, username: str, password: str) -> UserLoginSchema:
        ...
