from api.api_models import User
from api.api_models import Jwt


class IUserStorage:

    def create(self, user: User):
        raise NotImplemented

    def read(self, user_id: str) -> User:
        raise NotImplemented

    def update(self, user_id, user: User):
        raise NotImplemented

    def delete(self, user_id) -> User:
        raise NotImplemented


class ReadOnlyIUserStorage:
    def __init__(self, user_storage: IUserStorage):
        self.__user_storage = user_storage

    def read(self, user_id: str) -> User:
        return self.__user_storage.read(user_id)


class IJwtStorage:

    def create(self, jwt: Jwt):
        raise NotImplemented

    def read_by_user(self, user_id) -> list:
        raise NotImplemented

    def read_by_jwt(self, jwt: str) -> Jwt:
        raise NotImplemented

    def delete(self, jwt: str) -> str:
        raise NotImplemented

