from dataclasses import dataclass

from repository import UserRepository
from schema import UserLoginSchema
from exception import UserNotFoundException, UserNotCorrectPasswordException
from models import UserProfile


@dataclass
class AuthService:
    user_repository: UserRepository

    def login(self, username: str, password: str) -> UserLoginSchema:
        user = self.user_repository.get_user_by_username(username)
        self._validate_auth_user(user, password)
        return UserLoginSchema(user_id=user.id, access_token=user.access_token)

    @staticmethod
    def _validate_auth_user(user: UserProfile, password: str):
        """
        Этот метод статический, потому что он не обращается к другим атрибутам класса
        """
        if not user:
            raise UserNotFoundException
        if user.password != password:
            raise UserNotCorrectPasswordException
